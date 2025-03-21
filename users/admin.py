from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import  Volunteer, User, Slider, Document, MainData

# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

# admin.site.register(Job)
admin.site.register(Volunteer)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(MainData)