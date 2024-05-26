from django.urls import path
from .views import (home, volunteer_register, about_us, RegistrationView, 
                    LoginView, LogoutView, dashboard)

urlpatterns = [
    path("home/", home, name="home"),
    path("volunteer/", volunteer_register, name="volunteer"),
    path("about/", about_us, name='about'),
    path("register/", RegistrationView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("dashboard/", dashboard, name="dashboard"),
]