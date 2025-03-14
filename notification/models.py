from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import NotificationQuerySet
from users.models import User

# Create your models here.


class NotificationCategory(models.Model):
    name = models.CharField(_("نام"), max_length=100)
    slug = models.SlugField(_('اسلاگ'), max_length=255, unique=True)
    is_active = models.BooleanField(_("فعال"), default=True)

    date_added = models.DateTimeField(_("تاریخ افزودن"), auto_now_add=True)
    date_modify = models.DateTimeField(_("تاریخ آخرین تغییر"), auto_now=True)

    class Meta:
        db_table = 'notification_category'
        verbose_name = _('notification category')
        verbose_name_plural = _("notification categories")


    def __str__(self):
        return self.name or ""


class Notification(models.Model):
    users = models.ManyToManyField(User, verbose_name=_("کاربران"), related_name="notifications")
    category = models.ForeignKey(NotificationCategory, on_delete=models.CASCADE, null=True, blank=True)
    short_description = models.CharField(_("توضیح کوتاه"), max_length=150, null=True, blank=True)
    content = models.TextField(_("محتوا"), null=True, blank=True)
    link = models.URLField(_("لینک"), max_length=250, null=True, blank=True)
    date = models.DateTimeField(_("تاریخ"), null=True, blank=True)
    is_seen = models.BooleanField(_("دیده شده"), default=False)
    is_seen_by = models.ManyToManyField(
        User,
        verbose_name=_("دیده شده توسط"), 
        related_name="seen_notifications"
    )
    date_added = models.DateTimeField(_("تاریخ افزودن"), auto_now_add=True)
    date_modify = models.DateTimeField(_("تاریخ آخرین تغییر"), auto_now=True)

    objects = NotificationQuerySet.as_manager()

    def __str__(self):
        return f"{self.short_description}"