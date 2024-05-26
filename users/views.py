from django.core.validators import RegexValidator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages, auth
from django.views import View


import json, re
from Charity.settings import mail
from .forms import ContactUsForm, VolunteerRegisterForm
# Create your views here.

def home(request) :
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            subject = cd['subject']
            content = cd['content']
            message = "نام:{0}\n ایمیل:{1}\n پیام:{3}".format(name, email, content)
            send_mail(subject, message, mail, ['sevda.hayati2015@gmail.com'] ,fail_silently=False)
    else :
        form = ContactUsForm()
        context = {'form' : form}
    return render(request, "home.html", context)


def volunteer_register(request):
    if request.method == "POST":
        form = VolunteerRegisterForm(request.POST or None, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'به جمع داوطلبین خادمین سیده زینب خوش آمدید')
            return redirect('users:volunteer')
    form = VolunteerRegisterForm()
    return render(request, "users/volunteer.html", {"form": form})

def about_us(request) :
    return render (request, 'about.html')

_REGEX = re.compile(r'09(\d{9})$')

class PhoneValidationView(View) :
    def post(self, request) :
        data = json.loads(request.body)
        phone = data['phone']

        if not re.fullmatch(_REGEX, phone) :
            return JsonResponse({'PhoneValidationError' : 'شماره وارد شده صحیح نمیباشد'}, status=400)
        
        if User.objects.filter(phone=phone).exists :
            return JsonResponse({'PhoneError' : 'این شماره تماس قبلا استفاده شده'}, status=409)
        return JsonResponse({'username_valid' : True})
    

class RegistrationView(View) :
    def get(self, request) :
        return render(request, 'users/register.html')
    
    def post(self, request) :
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        context ={
            'fieldValues' : request.POST
        }
        if User.objects.filter(phone=phone).exists() :
            messages.error(request, 'این شماره تماس قبلا استفاده شده')
            return render(request, 'users/register.html')
        
        elif password1 != password2 :
            messages.error(request, 'رمز عبور مطابقت ندارد')
            return render(request, 'users/register.html', context)
        
        elif len(password1) < 4:
            messages.error(request, 'رمز عبور کوتاه است')
            return render(request, 'users/register.html', context)
        
        else :
            user = User.objects.create_user(phone=phone)
            if password1 is not None:
                user.set_password(password1)
            else:
                messages.error(request, "رمز عبور نمیتواند خالی باشد" , context)
                return render(request, 'users/register.html', context)
            user.save()
            messages.success(request, 'حساب کاربری با موفقیت ساخته شد')
            return user


class LoginView(View) :
    def get(self, request) :
        return render(request, 'users.login.html')
    
    def post(self,request) :
        phone = request.POST['phone']
        password1 = request.POST['pasword1']

        if phone and password1 :
            user = auth.authenticate(phone=phone, password=password1)
            if user :
                auth.login(request, user)
                messages.success(request, 'خوش اومدی')
        
            messages.error(request, 'شماره موبایل یا رمز عبور اشتباه است')
            return render(request, 'users/login.html')
        messages.error(request, 'لطفا شماره موبایل و رمز عبور را وارد کنید')
        return render(request, 'users/login.html')
    

class LogoutView(View) :
    def post(self, request) :
        auth.logout(request)
        messages.success(request, 'از حساب کاربری خارج شدید')
        return redirect('login')
    

@login_required(login_url='users/login')
def dashboard(request) :
    return render(request, 'users/dashboard.html')