from django import forms
from django.urls import reverse_lazy
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime

messages ={
    'required' : 'این فیلد نمیتواند خالی باشد',
    'max_length' : 'تعداد کاراکتر بیش از حد مجاز است',
    'invalid' : 'لطفا یک مقدار معتبر وارد کنید',
    'invalid_image' : 'لطفا یک تصویر معتبر وارد کنید',
    'invalid_choice' : 'لطفا یک گزینه معتبر را انتخاب کنید'
}

GENDER_CHOICES = (
    (1, 'مونث'),
    (2, 'مذکر'),
)

ABILITIES_CHOICES = (
    ("piping", "لوله کشی"),
    ("building", "بنا"),
    ("welder", "جوشکار"),
    ("electrician", "برقکار"),
    ("plaster", "گچ کار"),
    ("facilities", "تاسیسات"),
    ("graphist", "گرافیست"),
    ("programmer", "برنامه نویس"),
    ("photographer", "عکاس"),
    ("Cameraman", "فیلم بردار"),
    ("editor", "ویرایشگر"),
    ("content", "تولید محتوا"),
    ("speaker", "گوینده"),
    ("kindergarten", "مهدکودک"),
    ("translator", "مترجم عربی"),
    ("PA", "پزشک عمومی"),
    ("specialist", "پزشک متخصص"),
    ("psychologist", "روانشناس"),
    ("consult", "مشاوره"),
    ("dentist", "دندان پزشک"),
    ("pharmacist", "داروساز"),
    ("nurse", "پرستار"),
    ("executive", "پشتیبان اجرایی"),
    ("cook", "آشپز"),
    ("heavy vehicle", "راننده ماشین سنگین"),
    ("pickup truck", "راننده وانت"),
)

MARITAL_CHOICES = (
    (1, 'مجرد'),
    (2, 'متاهل'),
)

EDU_CHOICES = (
    (1, 'دیپلم'),
    (2, 'کاردانی'),
    (3, 'کارشناسی'),
    (4, 'کارشناسی ارشد'),
    (5, 'دکتری'),
)

EXP_CHOICES = (
    (1, 'دارم'),
    (2, 'ندارم'),
)


_REGEX = r'09(\d{9})$'
phone_validator = RegexValidator(_REGEX, "شماره وارد شده صحیح نمیباشد")


class VolunteerRegisterForm(forms.Form) :

    # def __init__(self, *args, **kwargs) :
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy("home")
    #     self.helper.add_input(Submit('ثبت', 'ثبت'))


    first_name = forms.CharField(max_length=100, label='نام', required=True, error_messages=messages)
    last_name = forms.CharField(max_length=100, label='نام خانوادگی', required=True, error_messages=messages)
    birth = forms.DateField(
        label='تاریخ تولد', 
        required=True, 
        error_messages=messages,
        widget = forms.DateInput(
            attrs ={'type' : 'date',
                    'max' : datetime.now().date()}
        ))
    nc = forms.NumberInput()
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        label='جنسیت', 
        required=True, 
        error_messages=messages,
        widget=forms.RadioSelect()
        )
    marital_status = forms.ChoiceField(
        choices= MARITAL_CHOICES, 
        label='وضعیت تاهل', 
        required=True, 
        error_messages=messages,
        widget = forms.RadioSelect()
        )
    phone = forms.CharField(max_length=14, validators=[phone_validator], label='شماره تماس', required=True, error_messages=messages)

    email = forms.EmailField(
        error_messages=messages,
        required=True,
        label='ایمیل')
    
    major = forms.CharField(max_length=100, label='رشته تحصیلی', required=True, error_messages=messages)
    education = forms.ChoiceField(choices=EDU_CHOICES, label='میزان تحصیلات', required=True, error_messages=messages)
    city = forms.CharField(max_length=100, label='شهر محل سکونت', required=True, error_messages=messages)
    abilities = forms.ChoiceField(
        error_messages=messages,
        required=True,
        choices=ABILITIES_CHOICES, 
        label='در چه زمینه ای میتوانید کمک کنید؟',
        widget=forms.CheckboxSelectMultiple()
        )
    
    specialist_info = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "در صورتی که پزشک متخصص هستید، نوع تخصص خود را وارد کنید",
                "class": "textarea is-success is-medium",
            }))

    profile_pic = forms.ImageField(
        error_messages=messages,
        upload_to = 'images/',
        required=True,
        label= "عکس پرسنلی",
        widget=forms.ClearableFileInput(attrs={
            'class' : 'form-control'
        }))
    
    experience = forms.ChoiceField(choices=EXP_CHOICES, label='سابقه کار جهادی', required=True, error_messages=messages)
    experience_info = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "در صورتی که سابقه کار جهادی دارید، توضیح دهید",
                "class": "textarea is-success is-medium",
            }))
    

class ContactUsForm(forms.Form) :
    name = forms.CharField(max_length=100, label='نام و نام خانوادگی')
    email = forms.EmailField(required=True, label='ایمیل')
    subject = forms.CharField(max_length=255, label='موضوع')
    content = forms.CharField(widget=forms.Textarea, required=True, label='پیام خود را بنویسید')