from django.urls import path
from .views import home, volunteer_register, about_us

urlpatterns = [
    path("home/", home, name="home"),
    path("volunteer/", volunteer_register, name="volunteer"),
    path("about/", about_us, name='about'),
]