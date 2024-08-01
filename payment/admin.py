from django.contrib import admin
from .models import Payment, PaymentMethod, PaymentCategory

# Register your models here.

admin.site.register(Payment)
admin.site.register(PaymentMethod)
admin.site.register(PaymentCategory)