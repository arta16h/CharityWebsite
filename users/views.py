from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages, auth
from django.views import View
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import re
from datetime import datetime, timedelta
import pytz

from .forms import VolunteerRegisterForm, NoPasswordRegisterForm, LoginForm, CustomUserChangeForm, DocumentForm
from .authentication import OtpAuthBackend
from .models import User, Slider, MainData
from utils.otp_tools import generate_otp_code, send_otp_code
# Create your views here.

def home(request) :
    main_data = MainData.objects.first()
    context = {
        'main_data' : main_data
    }
    return render(request, "home.html", context)


def volunteer_register(request):
    if request.user.is_authenticated and request.user.volunteer_info:
        messages.info(request, _("you has already registered as volunteer"))
        return redirect('dashboard')
    if request.method == "POST":
        form = VolunteerRegisterForm(request.POST or None, request.FILES)
        if form.is_valid():
            user = request.user
            if not user.is_authenticated:
                clean_data = form.cleaned_data.copy()
                register_form = NoPasswordRegisterForm(clean_data)
                user = register_form.save()

            volunteer_form = form.save()
            user.volunteer_info = volunteer_form
            user.save()
            messages.success(request, 'به جمع داوطلبین خادمین سیده زینب خوش آمدید')
            return redirect('dashboard')
        return render(request, "users/volunteer.html", {"form": form})
    prefill_data = {key: value for key , value in request.GET.items() if value}
    if request.user.is_authenticated:
        prefill_data.update({'first_name':request.user.first_name, 'last_name': request.user.last_name, 'phone':request.user.phone})
    form = VolunteerRegisterForm(initial=prefill_data)
    return render(request, "users/volunteer.html", {"form": form})

def about_us(request) :
    sliders = Slider.objects.all()
    context = {
        'sliders' : sliders
    }
    return render (request, 'about.html', context)

def contact_us(request) :
    return render (request, 'contact.html')

class PhoneValidationView(APIView) :
    def post(self, request) :
        data = request.POST
        phone = data['phone']
        validate_for = data['validate_for']
        if not re.fullmatch(re.compile(r'09(\d{9})$'), phone) :
            return JsonResponse({'message' : 'شماره وارد شده صحیح نمیباشد'}, status=400)
        if User.objects.filter(phone=phone).exists():
            if validate_for == 'register':
                return JsonResponse({'message' : 'این شماره تماس قبلا استفاده شده'}, status=409)
            elif validate_for == 'login':
                return JsonResponse({'message': _('Phone validated successfully')}, status=200)
        if validate_for == 'login':
            return JsonResponse({"message": _("user not found")}, status=400)
        return JsonResponse({'message' : True})
    

class EmailValidationView(APIView) :
    def post(self, request) :
        data = request.POST
        email = data['email']
        validate_for = data['validate_for']

        if not re.fullmatch(re.compile(r'^[^@]+@[^@]+\.[^@]+$'), email) :
            return JsonResponse({'message' : 'ایمیل وارد شده صحیح نمیباشد'}, status=400)
        
        if User.objects.filter(email=email).exists() :
            if validate_for == 'register':
                return JsonResponse({'message' : 'این ایمیل قبلا استفاده شده'}, status=409)
            elif validate_for == 'login':
                return JsonResponse({'message': _('ایمیل با موفقیت ارزیابی شد')}, status=200)
        if validate_for == 'login':
            return JsonResponse({"message": _("کاربر یافت نشد")}, status=400)
        return JsonResponse({'message' : True})


class RegistrationView(View) :
    def get(self, request) :
        if isinstance(request.user, User):
            messages.error(request, _('to create new account log out first'))
            return redirect("home")     
        return render(request, 'users/register.html')
    
    def post(self, request) :
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        context ={
            'fieldValues' : request.POST
        }
        if isinstance(request.user, User):
            messages.error(request, _('to create new account log out first'))
            return redirect("home")
        elif User.objects.filter(phone=phone).exists() :
            messages.error(request, 'این شماره تماس قبلا استفاده شده')
            return render(request, 'users/register.html')
        
        elif password1 != password2 :
            messages.error(request, 'رمز عبور مطابقت ندارد')
            return render(request, 'users/register.html', context)
        
        elif len(password1) < 4:
            messages.error(request, 'رمز عبور کوتاه است')
            return render(request, 'users/register.html', context)
        
        else :
            user = User.objects.create(phone=phone)
            if password1 is not None:
                user.set_password(password1)
            else:
                messages.error(request, "رمز عبور نمیتواند خالی باشد")
                return render(request, 'users/register.html', context)
            user.save()
            messages.success(request, 'حساب کاربری با موفقیت ساخته شد')
            auth.login(request, user, backend='users.authentication.UserAuthBackend')
            return redirect('dashboard')


class LoginView(View) :
    def get(self, request) :
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'users/login.html')
    
    def post(self,request) :
        login_form = LoginForm(request.POST)

        if login_form.is_valid() :
            login_data = login_form.cleaned_data
            user = auth.authenticate(
                request, 
                user_identifier=login_data["phone"],
                password=login_data["password"],
                backend="users.authentication.UserAuthBackend"
            )
            if user :
                auth.login(request, user, backend="users.authentication.UserAuthBackend")
                messages.success(request, 'خوش اومدی')
                return redirect('dashboard')
        
            messages.error(request, 'شماره موبایل یا رمز عبور اشتباه است')
            return render(request, 'users/login.html')
        messages.error(request, 'لطفا شماره موبایل و رمز عبور را وارد کنید')
        return render(request, 'users/login.html')
    

class LogoutView(View) :
    def get(self, request) :
        auth.logout(request)
        messages.success(request, 'از حساب کاربری خارج شدید')
        return redirect('login')
    

@login_required(login_url='login')
def dashboard(request) :
    print(request.FILES)
    user_update_form = CustomUserChangeForm(instance=request.user)
    if request.method == "POST":
        print(f"{request.POST=}")
        user_update_form = CustomUserChangeForm(
            request.POST, 
            request.FILES, 
            instance=request.user,
        )
        if user_update_form.is_valid():
            print("here")
            user_update_form.save()
            return redirect("dashboard")
        
    context = {
        "profile_update_form": user_update_form,
        'registered_days': (datetime.now(tz=pytz.timezone('Asia/Tehran')) - request.user.date_added).days
        }
    return render(request, 'users/dashboard.html', context=context)


class SendOtpView(APIView):
    
    def post(self, request):
        if request.user and request.user.is_authenticated:
            return Response(
                data={"data":None, "message":_("user is already logged in")},
                status=status.HTTP_400_BAD_REQUEST
            )
        otp_type = request.POST.get("otp_type")
        otp_identifier = request.POST.get("otp_identifier")
        if otp_type in ["sms", "email"]:
            if otp_identifier:
                otp_code = generate_otp_code()
                print(f"{otp_code=}")
                request.session['otp_code'] = otp_code
                request.session['otp_identifier'] = otp_identifier
                request.session['otp_expire_time'] = str(datetime.now() + timedelta(seconds=int(settings.OTP_EXPIRE_TIME)))
                send_otp_code(otp_code, otp_type, otp_identifier)
                message = _("code has sent to {otp_identifier}").format(otp_identifier=otp_identifier)
                return Response(
                    data={"data":None, "message":message},
                    status=status.HTTP_200_OK
                )
            return Response(
                data={"data":None, "message":_("otp identifier has bot provided")},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data={"data":None, "message":_("invalid otp type")},
            status=status.HTTP_400_BAD_REQUEST
        )

class VerifyOtpView(APIView):

    def post(self, request):
        otp_request = request.query_params.get("otp_request")
        if otp_request == "login":
            return self.verify_login_otp(request)
        if otp_request == "verify_otp":
            return self.verify_otp(request)
        else:
            return Response(
                data={"data": None, "message":_("invalid otp request type")},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def verify_login_otp(self, request):
        otp_code = request.POST.get("otp_code")
        user = OtpAuthBackend().authenticate(request, otp_code=otp_code)
        if user:
            auth.login(request, user, backend="users.authentication.UserAuthBackend")
            del request.session["otp_code"]
            del request.session["otp_expire_time"]
            del request.session["otp_identifier"]
            message =  _('You have logged in successfully')
            messages.success(request, message)
            return Response(
                    data={"data":None, "message":message},
                    status=status.HTTP_200_OK
            )
        messages.error(request, _('invalid otp'))
        return Response(
            data={"data":None, "message":_("invalid otp")},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def verify_otp(self, request):
        otp_code = request.POST.get("otp_code")
        if OtpAuthBackend().verify_otp(request, otp_code=otp_code):
            return Response(
                    data={"data":None, "message":_("otp veified successfully")},
                    status=status.HTTP_200_OK
            )
        messages.error(request, _('invalid otp'))
        return Response(
            data={"data":None, "message":_("invalid otp")},
            status=status.HTTP_400_BAD_REQUEST
        )
    
def donate(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you for your donation!')
        return redirect('donate')
    return render(request, 'donate.html')

@login_required(login_url='login')
def upload(request) :
    form = DocumentForm

    if request.method == 'POST' :
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() :
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            messages.success(request, 'مدارک شما با موفقیت ارسال شد')
            return redirect('dashboard')
        messages.error(request, 'عملیات با خطا مواجه شد')
    else:
        form = DocumentForm()
        return render(request, "users/upload.html")