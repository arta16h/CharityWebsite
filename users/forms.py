from django import forms
from django.urls import reverse_lazy
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_jalali.forms import jDateInput
from django_jalali.admin.widgets import AdminjDateWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from .models import User
from .models import Volunteer

from typing import Any

messages ={
    'required' : 'این فیلد نمیتواند خالی باشد',
    'max_length' : 'تعداد کاراکتر بیش از حد مجاز است',
    'invalid' : 'لطفا یک مقدار معتبر وارد کنید',
    'invalid_image' : 'لطفا یک تصویر معتبر وارد کنید',
    'invalid_choice' : 'لطفا یک گزینه معتبر را انتخاب کنید'
}

class VolunteerRegisterForm(forms.ModelForm):
    error_css_class = "error"
    required_css_class = "required"
    class Meta:
        model = Volunteer
        fields = '__all__'
        widgets = {
            'gender': forms.Select(),
            'birth': jDateInput(attrs={'widgets' : 'AdminjDateWidget'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'text-end p-1 m-1'}),
            'experience_info': forms.Textarea(attrs={
                'class': 'text-end p-1 m-1', 
                "placeholder": "در صورتی که سابقه کار جهادی دارید، توضیح دهید"
            }),
            'specialist_info': forms.Textarea(attrs={
                'class': 'text-end p-1 m-1', 
                "placeholder": "در صورتی که پزشک متخصص هستید، نوع تخصص خود را وارد کنید"
            }),
            'abilities': forms.Select(attrs={
                'class': 'text-end p-1 m-1'
            }),
        }
        labels = {
            'abilities': 'در چه زمینه ای میتوانید کمک کنید؟',
            'gender' : 'جنسیت',
            'birth' : 'تاریخ تولد',
            'email' : 'ایمیل',
            'profile_pic' : 'عکس پرسنلی',
            'education' : 'تحصیلات',
            'experience_info' : 'سابقه کار جهادی',
            'specialist_info' : 'تخصص',
            'nc' : 'کدملی',
            'major' : 'رشته تحصیلی',
            'marital_status' : 'وضعیت تاهل',
            'phone' : 'شماره تماس',
            'city' : 'شهر محل سکونت'
        }
        error_messages = messages

    def __init__(self, *args, **kwargs):
        super(VolunteerRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + "text-end form-control"


# class ContactUsForm(forms.Form) :
#     name = forms.CharField(max_length=100, label='نام و نام خانوادگی')
#     email = forms.EmailField(required=True, label='ایمیل')
#     subject = forms.CharField(max_length=255, label='موضوع')
#     content = forms.CharField(widget=forms.Textarea, required=True, label='پیام خود را بنویسید')


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['phone','username','email','password1','password2'] 

    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + "text-end form-control"

class NoPasswordRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['phone', 'first_name', 'last_name', 'email', 'city']

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + "text-end form-control"
            visible.field.widget.attrs['form'] = "profile_update_form"

    class Meta:
        model=User
        fields=['first_name', 'last_name','phone', 'email', 'city', 'image']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),            
        }