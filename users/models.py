from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from utils.file_path_creator import make_image_path
from django.utils.translation import gettext_lazy as _
from .enums import *
from .manager import UserManager
from PIL import Image
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

    class Meta :
        verbose_name = _("داوطلب")
        verbose_name_plural = _("داوطلب ها")



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_("نام"), max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("نام خانوادگی"), max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name=_("ایمیل"), unique=True, null=True, blank=True)    
    city = models.CharField(verbose_name=_("شهر محل سکونت"), max_length=100, null=True, blank=True)
    phone = models.CharField(
        verbose_name=_("شماره تماس"),
        max_length=14, 
        validators=[RegexValidator(r'09(\d{9})$')], 
        unique=True,
        blank=True
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

    def save(self) :
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.image.path)

    class Meta :
        verbose_name = _("عضو")
        verbose_name_plural = _("اعضا")

class DocumentCategory(models.Model):
    name = models.CharField(_("نام"), max_length=100)
    slug = models.SlugField(_('اسلاگ'), max_length=255, unique=True)
    is_active = models.BooleanField(_("فعال"), default=True)

    date_added = models.DateTimeField(_("تاریخ افزودن"), auto_now_add=True)
    date_modify = models.DateTimeField(_("تاریخ آخرین تغییر"), auto_now=True)

    class Meta:
        db_table = 'document_category'
        verbose_name = _('نوع مدرک')
        verbose_name_plural = _("انواع مدارک")


    def __str__(self):
        return self.name or ""
    

class Document(models.Model) :
    filename = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("نام فایل"))
    file = models.FileField(upload_to='documents/',verbose_name=_("مدارک"))
    category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("توضیحات"))
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta :
        verbose_name = _("مدرک")
        verbose_name_plural = _("مدارک")
    

class Slider(models.Model) :
    title = models.CharField(max_length=255, verbose_name=_("عنوان"))
    link = models.URLField(max_length=255, verbose_name=_("لینک"))
    description = models.TextField(verbose_name=_("توضیحات"))
    image = models.ImageField(upload_to='images/slider')

    class Meta :
        verbose_name = _("اسلایدر")
        verbose_name_plural = _("اسلایدرها")


class MainData(models.Model) :
    phone = models.CharField(verbose_name=_("شماره موکب"), max_length=14, validators=[RegexValidator(r'09(\d{9})$')], null=True, blank=True)
    email = models.EmailField(verbose_name=_("ایمیل"), null=True, blank=True)
    credit = models.CharField(verbose_name=_("شماره کارت"), max_length=16, null=True, blank=True)
    address = models.CharField(verbose_name=_("آدرس"), max_length=255, null=True, blank=True)
    igurl = models.URLField(max_length=255, verbose_name=_("لینک اینستاگرام"), null=True, blank=True)
    telurl = models.URLField(max_length=255, verbose_name=_("لینک تلگرام"), null=True, blank=True)
    eturl = models.URLField(max_length=255, verbose_name=_("لینک ایتا"), null=True, blank=True)
    homeh1 = models.CharField(verbose_name=_("تیتر اول صفحه اصلی"), max_length=255, null=True, blank=True)
    homeh2 = models.CharField(verbose_name=_("تیتر دوم صفحه اصلی"), max_length=255, null=True, blank=True)
    homeh3 = models.CharField(verbose_name=_("متن اول صفحه اصلی"), max_length=255, null=True, blank=True)
    logo = models.ImageField(verbose_name=_("لوگو"), upload_to="logo/", null=True, blank=True)
    home = models.ImageField(verbose_name=_("عکس صفحه اصلی"), upload_to="home/", null=True, blank=True)
    footerabout = models.CharField(verbose_name=_("اطلاعات فوتر"), max_length=255, null=True, blank=True)

    class Meta :
        verbose_name = _("اطلاعات")
        verbose_name_plural = _("اطلاعات")
    
