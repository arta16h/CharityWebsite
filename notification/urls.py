from django.urls import path
from .views import SendNotification, MarkNotificatoinAsRead

urlpatterns = [
    path("send-notification/", SendNotification.as_view(), name="send_notification"),
    path("mark-notification-as-read/", MarkNotificatoinAsRead.as_view(), name="mark_notification_as_read"),
]