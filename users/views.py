from django.shortcuts import render, redirect
from django.core.mail import send_mail

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
        form = VolunteerRegisterForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('users:volunteer')
    form = VolunteerRegisterForm()
    return render(request, "users/volunteer.html", {"form": form})