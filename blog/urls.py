from .views import BlogListView
from django.urls import path

urlpatterns =[
    path('lists/', BlogListView.as_view(), name='blog-list'),
]