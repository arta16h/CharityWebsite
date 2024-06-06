from django.shortcuts import render
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.

class BlogListView(LoginRequiredMixin, ListView) :
    model = Blog
    template_name = 'blog/blog-list'
    context_object_name = 'blog'
    ordering = ["-created_at"]


class BlogDetailView(LoginRequiredMixin, DetailView) :
    model = Blog
    template_name = 'blog/blog-detail'


class BlogCreateView(LoginRequiredMixin, CreateView) :
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/new-blog'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class BlogUpdateView(LoginRequiredMixin, UpdateView) :
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)