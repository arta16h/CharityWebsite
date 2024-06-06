from .views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns =[
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]