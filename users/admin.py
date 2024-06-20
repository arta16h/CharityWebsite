from django.contrib import admin
from .models import  Volunteer, User

# Register your models here.

# admin.site.register(Job)
admin.site.register(Volunteer)
admin.site.register(User)