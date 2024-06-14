# In the name of GOD

from django.utils.translation import gettext_lazy as _

FEMALE = 1
MALE = 2

SINGLE = 1
MARIED = 2

DIPLOMA = 1
ASSOCIATE = 2
BSC = 3
MSC = 4
PHD = 5

GENDER_CHOICES = (
    (FEMALE, _('مونث')),
    (MALE, _('مذکر')),
)

MARITAL_CHOICES = (
    (SINGLE, _("مجرد")),
    (MARIED, _("متاهل")),
)

# EDU_CHOICES = (
#     (DIPLOMA, _('diploma')),
#     (ASSOCIATE, _('associate degree')),
#     (BSC, _('Bsc')),
#     (MSC, _('Msc')),
#     (PHD, _('Phd')),
# )

EDU_CHOICES = (
    (DIPLOMA, 'دیپلم'),
    (ASSOCIATE, 'کاردانی'),
    (BSC, 'کارشناسی'),
    (MSC, 'کارشناسی ارشد'),
    (PHD, 'دکتری'),
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
