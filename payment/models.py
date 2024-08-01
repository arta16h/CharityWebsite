from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class PaymentCategory(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    slug = models.SlugField(_("اسلاگ"), null=False, blank=False)
    description = models.CharField(_("توضیحات"), max_length=250, null=True, blank=True)
    is_active = models.BooleanField(_("فعال است"), default=True)
    image = models.ImageField(_("تصویر"), upload_to='payment_category_images/', null=True, blank=True)

    date_added = models.DateTimeField(_("تاریخ افزودن"), auto_now_add=True)
    date_modify = models.DateTimeField(_("تاریخ تغییر"), auto_now=True)

    class Meta:
        db_table = 'payment_category'
        verbose_name = _('دسته پرداخت')
        verbose_name_plural = _("دسته های پرداخت")

    def __str__(self):
        return str(self.name)


class PaymentMethod(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"), null=False, blank=False)
    description = models.CharField(_("description"), max_length=250, null=True, blank=True)
    is_active = models.BooleanField(_("is active"), default=True)
    image = models.ImageField(_("image"), upload_to='payment_method_images/', null=True, blank=True)

    date_added = models.DateTimeField(_("date added"), auto_now_add=True)
    date_modify = models.DateTimeField(_("date modify"), auto_now=True)

    class Meta:
        db_table = 'payment_method'
        verbose_name = _('روش پرداخت')
        verbose_name_plural = _("روش های پرداخت")

    def __str__(self):
        return str(self.name)


class Payment(models.Model):
    STATUS_PEND = 1
    STATUS_IN_PROGRESS = 2
    STATUS_DOING = 3
    STATUS_DONE = 4
    STATUS_FAIL = 5

    PAYMENT_STATUS_CHOICES_VIEW = {
        STATUS_PEND: _("در انتظار"),
        STATUS_IN_PROGRESS: _("در پروسه انجام"),
        STATUS_DOING: _("در حال انجام"),
        STATUS_DONE: _("انجام یافته"),
        STATUS_FAIL: _("ناموفق"),
    }
    PAYMENT_STATUS_CHOICES = (
        (STATUS_PEND, "در انتظار"),
        (STATUS_IN_PROGRESS, "در پروسه انجام"),
        (STATUS_DOING, "در پروسه انجام"),
        (STATUS_DONE, "در پروسه انجام"),
        (STATUS_FAIL, "در پروسه انجام"),
    )

    payment_trace_id = models.UUIDField(_("payment_id"), max_length=150, unique=True)
    request_user = models.ForeignKey(User, verbose_name=_("request user"), on_delete=models.CASCADE)
    payment_status = models.PositiveSmallIntegerField(_("payment_status"), choices=PAYMENT_STATUS_CHOICES)
    payment_method = models.ForeignKey(PaymentMethod, verbose_name=_("payment method"), on_delete=models.CASCADE)
    request_time = models.DateTimeField(_("request time"))
    total_amount = models.PositiveBigIntegerField(_("total amount"))
    pay_id = models.CharField(_("pay id"), max_length=30, unique=True)
    image = models.ImageField(_("image"), upload_to='payment_images/', null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)

    date_added = models.DateTimeField(_("date added"), auto_now_add=True)
    date_modify = models.DateTimeField(_("date modify"), auto_now=True)

    def __str__(self):
        return f'{self.payment_method} {self.payment_trace_id} {self.PAYMENT_STATUS_CHOICES_VIEW[self.payment_status]}'

    @classmethod
    def generate_unique_payment_code(cls, user_id, amount):
        return f"{str(int(user_id)*4)}{amount}"

    class Meta:
        db_table = 'payment'
        verbose_name = _('پرداخت')
        verbose_name_plural = _("پرداخت ها")