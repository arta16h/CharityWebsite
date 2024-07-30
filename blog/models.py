from django.db import models
from django.urls import reverse
from users.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")
    
User = settings.AUTH_USER_MODEL    
class Blog(models.Model) :
    title = models.CharField(max_length = 255, verbose_name=_('عنوان'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('نویسنده'))
    content = models.TextField(verbose_name=_('متن'))
    category = models.ManyToManyField(Category, blank=True, verbose_name=_('دسته بندی'))
    keywords = models.TextField(null=True, blank=True, verbose_name=_('کلمات کلیدی'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('تصویر'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.title}"
    
    def get_absolute_url(self) :
        return reverse('blog-detail', kwargs={'pk':self.pk})
    
    class Meta :
        verbose_name = _("بلاگ")
        verbose_name_plural = _("بلاگ ها")


class Events(models.Model) :
    title = models.CharField(max_length = 255, verbose_name=_('عنوان'))
    content = models.TextField(verbose_name=_('توضیحات'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('تصویر'))
    since = models.DateField(verbose_name=_('تاریخ شروع'))
    till = models.DateField(verbose_name=_('تاریخ اتمام'))
    place = models.CharField(max_length = 255, verbose_name=_('مکان'))
    number = models.IntegerField(verbose_name=_('ظرفیت'))
    volunteers = models.ManyToManyField(User, verbose_name=_('داوطلبان'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = _("اردو")
        verbose_name_plural = _("اردو ها")