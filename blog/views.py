from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import json

# Create your views here.

class BlogListView(LoginRequiredMixin, ListView) :
    model = Blog
    template_name = 'blog/blog-list.html'
    context_object_name = 'blog'
    ordering = ["-created_at"]
    paginate_by = 7

class BlogDetailView(LoginRequiredMixin, DetailView) :
    model = Blog
    template_name = 'blog/blog-detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView) :
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/new-blog.html'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        blog = self.get_object()
        if self.request.user == blog.author :
            return True
        return False
    

class BlogDeleteView(DeleteView) :
    model = Blog
    success_url = 'blog-list'

    def test_func(self) -> bool | None:
        blog = self.get_object()
        if self.request.user == blog.author :
            return True
        return False
    

def search_blog(request) :
    if request.method == 'POST' :
        search_str = json.loads(request.body).get("serachText")
        blog = Blog.objects.filter(title__contains=search_str, owner=request.user) | Blog.objects.filter(
            author__contains=search_str, owner=request.user) | Blog.objects.filter(
                content__contains=search_str, owner=request.user) | Blog.objects.filter(
                    category__contains=search_str, owner=request.user) | Blog.objects.filter(
                        keywords__contains=search_str, owner=request.user)
        data = blog.values()
        return JsonResponse(list(data), safe=False)