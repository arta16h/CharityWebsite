from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .helper import make_image_path
from django.utils.translation import gettext_lazy as _
from .enums import *
# Create your models here.

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
phone_validator = RegexValidator(_REGEX)

class Volunteer(models.Model) :

class User(AbstractUser):
    first_name = models.CharField(verbose_name=_("first name"), max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("last name"), max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name=_("email"), unique=True, null=True, blank=True)    
    city = models.CharField(verbose_name=_("city"), max_length=100, null=True, blank=True)
    phone = models.CharField(
        verbose_name=_("phone"),
        max_length=14, 
        validators=[phone_validator], 
        unique=True
    )
    volunteer_info = models.OneToOneField(Volunteer, on_delete=models.SET_NULL, null=True, blank=True)