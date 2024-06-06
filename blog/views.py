from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView

# Create your views here.

class BlogListView(ListView) :
    model = Blog