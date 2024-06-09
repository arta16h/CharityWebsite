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

class Job(models.Model):
    en_name = models.CharField(_("english name"), max_length=60)
    fa_name = models.CharField(_("persian name"), max_length=60, null=True, blank=True)
    description = models.CharField(_("description"), max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(_("date added"), auto_now=True)
    date_modified = models.DateTimeField(_("date modified"), auto_now_add=True)

    def __str__(self) -> str:
        return self.fa_name or self.en_name

class Volunteer(models.Model) :
    first_name = models.CharField(verbose_name=_("first name"), max_length=100)
    last_name = models.CharField(verbose_name=_("last name"), max_length=100)
    email = models.EmailField(verbose_name=_("email"), unique=True)    
    birth = models.DateField(verbose_name=_("birth day"))
    nc = models.IntegerField(verbose_name=_("nc"))
    major = models.CharField(verbose_name=_("major"), max_length=100)
    city = models.CharField(verbose_name=_("city"), max_length=100)
    phone = models.CharField(
        verbose_name=_("phone"),
        max_length=14, 
        validators=[phone_validator], 
        unique=True
    )
    specialist_info = models.TextField(verbose_name=_("specialist info"))
    profile_pic = models.ImageField(verbose_name=_("profile picture"), upload_to=make_image_path(first_name, last_name))   
    abilities = models.ManyToManyField(verbose_name=_("abilities"), to=Job)
    marital_status = models.PositiveSmallIntegerField(
        verbose_name=_("marital status"),
        choices= MARITAL_CHOICES
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name=_("gender"), 
        choices=GENDER_CHOICES
    )
    education = models.PositiveSmallIntegerField(
        verbose_name=_("education"), 
        choices=EDU_CHOICES
    )
    experience = models.BooleanField(
        verbose_name=_("voulunteer exprience"),
    )
    experience_info = models.TextField(verbose_name=_("experience info"))



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