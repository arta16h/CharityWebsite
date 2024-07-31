from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Notification, NotificationCategory
from .forms import CreateNotificationForm
from users.models import User, Volunteer
# Create your views here.
class SendNotification(APIView) :
    permission_classes = [IsAdminUser]

    def post(self, request) :
        data = request.POST
        notif_form = CreateNotificationForm(data)

        if notif_form.is_valid():
            notification = notif_form.save()
            users = User.objects.all()
            if abilities:=data.getlist("specialist_filter", []):
                users = users.filter(
                    id__in=list(
                        Volunteer.objects.filter(abilities__in=abilities).values_list("user", flat=True)
                    )
                )
            if user_ids_filter:=data.getlist("user_ids_filter", []):
                users = users.filter(id__in=user_ids_filter)
            notification.users.add(*users)
            notification.save()
            return Response(data={"message": "پیام با موفقیت ارسال شد"}, status=200)
        return Response(data={"message":str(notif_form.errors)}, status=400)
