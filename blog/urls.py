from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView
from django.urls import path

urlpatterns =[
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', BlogCreateView.as_view(), name='new-blog'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
]