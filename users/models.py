from django.db import models
from django.core.validators import RegexValidator

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
    first_name = models.CharField(max_length=100, required=True)
    last_name = models.CharField(max_length=100, required=True)
    birth = models.DateField(required=True)
    nc = models.IntegerField(max_length=10)
    gender = models.CharField(
        max_length=10
        choices=GENDER_CHOICES, 
        required=True, 
        )
    marital_status = models.CharField(
        max_length=10
        choices= MARITAL_CHOICES, 
        required=True,
        )
    
    phone = models.CharField(max_length=14, validators=[phone_validator], required=True)
    email = models.EmailField(required=True)    
    major = models.CharField(max_length=100, required=True)
    education = models.CharField(max_length=25, choices=EDU_CHOICES, required=True)
    city = models.CharField(max_length=100, required=True)
    abilities = models.CharField(max_length=50, required=True, choices=ABILITIES_CHOICES, )    
    specialist_info = models.TextField()
    profile_pic = models.ImageField(required=True, upload_to='images/')   
    experience = models.CharField(max_length=10, choices=EXP_CHOICES, required=True)
    experience_info = models.TextField()

