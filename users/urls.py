from django.urls import path
from .views import home, volunteer_register

urlpatterns = [
    path("home/", home, name="home"),
    path("volunteer/", volunteer_register, name="volunteer"),
]