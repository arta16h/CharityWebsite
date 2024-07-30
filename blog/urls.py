from .views import (BlogListView, BlogDetailView, BlogCreateView, 
                    BlogUpdateView, BlogDeleteView, search_blog, 
                    EventDetailView, EventListView, search_event)
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns =[
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', BlogCreateView.as_view(), name='new-blog'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/search-blog', csrf_exempt(search_blog), name='search_blog'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/search-event', csrf_exempt(search_event), name='search_event'),
]