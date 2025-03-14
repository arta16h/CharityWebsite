from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Volunteer, User, Slider, Document, MainData

# Register your models here.

# admin.site.register(Job)
admin.site.register(Volunteer)
admin.site.register(User, UserAdmin)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(MainData)