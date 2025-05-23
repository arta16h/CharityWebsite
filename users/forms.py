from django import forms
from django.urls import reverse_lazy
from django_jalali.forms import jDateField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Volunteer, Document
from persiantools.jdatetime import JalaliDate
from typing import Any
from django.utils.translation import gettext_lazy as _

from jalali_date.widgets import AdminJalaliDateWidget
from jalali_date.fields import JalaliDateField

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

    # def clean_birth(self):
    #     jalali_date = self.cleaned_data['birth']
    #     try:
    #         gregorian_date = JalaliDate.strptime(jalali_date, "%Y/%m/%d").to_gregorian()
    #         return gregorian_date
    #     except:
    #         raise forms.ValidationError("تاریخ وارد شده معتبر نیست")

    def clean_birth(self):
        return self.cleaned_data['birth']

    def __init__(self, *args, **kwargs):
        super(VolunteerRegisterForm, self).__init__(*args, **kwargs)
        self.fields['birth'] = JalaliDateField(label=_('تاریخ تولد'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + " text-end form-control"



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

class CustomUserChangeForm(forms.ModelForm):
    phone = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + "text-end form-control form-control-prof"
            visible.field.widget.attrs['form'] = "profile_update"

    class Meta:
        model=User
        fields=['first_name', 'last_name','phone', 'email', 'city', 'image']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),            
        }

class DocumentForm(forms.ModelForm) :

    class Meta :
        model= Document
        fields=['filename', 'file', 'description']
        widgets = {
            'file' : forms.ClearableFileInput()
        }
        labels = {
        'filename' : 'نام فایل',
        'file' : 'فایل',
        'description' : 'توضیحات'
        }
        error_messages = messages