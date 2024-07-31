from django.db import models

class NotificationQuerySet(models.QuerySet):
    def unread_notifications(self):
        return self.filter(is_seen=False)