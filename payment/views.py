# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from notification.models import Notification, NotificationCategory
from users.models import User
from .models import Payment, PaymentMethod, PaymentCategory
# Create your views here.



class DonateView(View):
    
    def get(self, request):
        context = {
            "payment_categories": PaymentCategory.objects.all(),
            "payment_methods": PaymentMethod.objects.all(),
        }
        return render(request, 'donate.html', context)
    
    def post(self, request):
        messages.success(request, 'Thank you for your donation!')
        return redirect('donate')
