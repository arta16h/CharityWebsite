from django.contrib import admin
from .models import  Volunteer, User, Slider, Document, MainData

# Register your models here.

# admin.site.register(Job)
admin.site.register(Volunteer)
admin.site.register(User)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(MainData)