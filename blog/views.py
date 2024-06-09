from django.shortcuts import render
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class BlogListView(LoginRequiredMixin, ListView) :
    model = Blog
    template_name = 'blog/blog-list'
    context_object_name = 'blog'
    ordering = ["-created_at"]
    paginate_by = 7

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