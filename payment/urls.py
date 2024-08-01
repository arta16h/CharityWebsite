from django.urls import path

from .views import DonateView


urlpatterns = [
    path("donate/", DonateView.as_view(), name="donate"),
]