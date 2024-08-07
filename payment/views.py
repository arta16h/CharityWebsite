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

import json
import uuid
from datetime import datetime
# Create your views here.



class DonateView(View):
    
    def get(self, request):
        context = {
            "payment_categories": PaymentCategory.objects.all(),
            "payment_methods": PaymentMethod.objects.all(),
        }
        return render(request, 'donate.html', context)
    
    def post(self, request):
        form_data = request.POST
        if form_data.get("payment_method") == "cart_to_cart":
            trace_id = uuid.uuid4()
            if Payment.objects.filter(payment_trace_id=form_data.get("trace_id")).exists():
                messages.error(request, 'پرداخت با این شناسه پیگیری قبلا ثبت شده است')
                return redirect('donate')
            Payment.objects.create(
                payment_trace_id=form_data.get("trace_id"),
                payment_service_trace_id=trace_id,
                request_user=request.user if request.user.is_authenticated else None,
                payment_category_id=int(form_data.get("payment_category") )if form_data.get("payment_category", "").isdecimal() else None,
                payment_status=Payment.STATUS_DONE,
                payment_method=PaymentMethod.objects.get(name="cart_to_cart"),
                request_time=datetime.now(),
                total_amount=form_data.get("amount"),
                description=form_data.get("message")
            )
            context = {"payment_trace_id": trace_id, "status": True}
            response = render(request, "payment/payment_confirm.html", context)
            if request.user.is_anonymous:
                donates = json.loads(request.COOKIES.get("donates", "[]"))
                donates.append({"payment_data": form_data, "payment_trace_id": str(trace_id)})
                response.set_cookie("donates", json.dumps(donates))
            return response
        messages.success(request, 'Thank you for your donation!')
        return redirect('donate')
