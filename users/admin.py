from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
import django.forms as forms
import django_jalali.admin as jadmin
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
class VolunteerAdminForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        widgets = {
            'birth': jadmin.widgets.AdminjDateWidget,
        }


class VolunteerAdmin(jadmin.ModelAdmin):
    form = VolunteerAdminForm
    list_display = ('name', 'birth')
    search_fields = ('name',)
    list_filter = ('birth',)
# admin.site.register(Job)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(MainData)