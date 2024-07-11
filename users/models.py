from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from utils.file_path_creator import make_image_path
from django.utils.translation import gettext_lazy as _
from .enums import *
from .manager import UserManager
from django_jalali.db.models import jDateField
# Create your models here.


class Volunteer(models.Model) :
    first_name = models.CharField(verbose_name=_("نام"), max_length=100)
    last_name = models.CharField(verbose_name=_("نام خانوادگی"), max_length=100)
    email = models.EmailField(verbose_name=_("ایمیل"), unique=True)    
    birth = jDateField(verbose_name=_("تاریخ تولد"))
    nc = models.CharField(verbose_name=_("کدملی"), max_length=10, unique=True)
    major = models.CharField(verbose_name=_("رشته تحصیلی"), max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name=_("شهر محل سکونت"), max_length=100, null=True, blank=True)
    phone = models.CharField(
        verbose_name=_("شماره تماس"),
        max_length=14, 
        validators=[RegexValidator(r'09(\d{9})$')], 
        unique=True
    )
    specialist_info = models.TextField(verbose_name=_("تخصص"), null=True, blank=True)
    profile_pic = models.ImageField(verbose_name=_("عکس پرسنلی"), upload_to=make_image_path, null=True, blank=True)   
    abilities = models.CharField(max_length= 100, choices=ABILITIES_CHOICES, default='لوله کشی', verbose_name=_("توانایی ها"))
    marital_status = models.PositiveSmallIntegerField(
        verbose_name=_("وضعیت تاهل"),
        choices= MARITAL_CHOICES,
        default='مجرد'
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name=_("جنسیت"), 
        choices=GENDER_CHOICES,
        default= 'مذکر'
    )
    education = models.PositiveSmallIntegerField(
        verbose_name=_("تحصیلات"), 
        choices=EDU_CHOICES,
        null=True, blank=True
    )
    experience_info = models.TextField(verbose_name=_("سابقه کار جهادی"), null=True, blank=True)



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_("نام"), max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("نام خانوادگی"), max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name=_("ایمیل"), unique=True, null=True, blank=True)    
    city = models.CharField(verbose_name=_("شهر محل سکونت"), max_length=100, null=True, blank=True)
    phone = models.CharField(
        verbose_name=_("شماره تماس"),
        max_length=14, 
        validators=[RegexValidator(r'09(\d{9})$')], 
        unique=True
    )
    username = models.CharField(_("نام کاربری"), max_length=50, null=True, blank=True)
    image = models.ImageField(verbose_name=_("عکس پروفایل"), upload_to="users/images", null=True, blank=True)   
    volunteer_info = models.OneToOneField(Volunteer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('اطلاعات داوطلبی'))

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.phone) or str(self.username)
    
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        if self.email:
            send_mail(subject, message, from_email, [self.email], **kwargs)