from django.contrib import admin
from .models import Blog, Category, Events

# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Events)