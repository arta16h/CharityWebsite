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


