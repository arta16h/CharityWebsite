from django.contrib import admin
from .models import Notification, NotificationCategory

# Register your models here.
admin.site.register(Notification)
admin.site.register(NotificationCategory)