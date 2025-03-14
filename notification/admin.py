from django.contrib import admin
from .models import Notification, NotificationCategory
from users.models import User

# Register your models here.

class SendedUserInline(admin.TabularInline):
    verbose_name = "sended to user"
    model = Notification.users.through
    extra = 0


class SeenByUsersInline(admin.TabularInline):
    verbose_name = "read by user"
    model = Notification.is_seen_by.through
    extra = 0


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    inlines = [
        SendedUserInline,
        SeenByUsersInline
    ]
    exclude = ["users"]
    readonly_fields = ("is_seen_by", )

admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationCategory)