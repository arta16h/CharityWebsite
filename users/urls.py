from django.urls import path
from .views import (
    home, volunteer_register, about_us, dashboard, contact_us, donate,
    RegistrationView, LoginView, LogoutView, SendOtpView, upload,
    VerifyOtpView, PhoneValidationView, EmailValidationView,
)
from .staff_views import staff_dashboard

urlpatterns = [
    path("home/", home, name="home"),
    path("donate/", donate, name="donate"),
    path("upload/", upload, name="upload"),
    path("about/", about_us, name='about'),
    path("contact/", contact_us, name='contact'),
    path("dashboard/", dashboard, name="dashboard"),
    path("staff_dashboard/", staff_dashboard, name="staff_dashboard"),
    path("volunteer/", volunteer_register, name="volunteer"),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("send_otp/", SendOtpView.as_view() , name="send_otp"),
    path("register/", RegistrationView.as_view(), name='register'),
    path("verify_otp/", VerifyOtpView.as_view(), name="verify_otp"),
    path("validate_email/", EmailValidationView.as_view(), name="validate_email"),
    path("validate_phone/", PhoneValidationView.as_view(), name="validate_phone"),
]