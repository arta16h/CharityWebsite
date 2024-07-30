from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from notification.forms import CreateNotificationForm
from .models import User
from .enums import ABILITIES_CHOICES

@login_required(login_url="login")
def staff_dashboard(request):
    if not request.user.is_staff:
        return redirect("home")
    notification_form = CreateNotificationForm()
    context = {
        "notification_form": notification_form,
        "specializations": ABILITIES_CHOICES,
        "users": User.objects.all()
    }
    return render(request, "users/staff_dashboard.html", context)