from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.

class BlogListView(ListView) :
    model = Blog
    template_name = 'blog/blog-list'
    context_object_name = 'blog'
    ordering = ["-created_at"]


class BlogDetailView(DetailView) :
    model = Blog