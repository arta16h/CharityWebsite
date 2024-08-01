# Generated by Django 5.0.6 on 2024-07-29 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_remove_notification_user_notification_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 7, 29, 20, 51, 50, 655466, tzinfo=datetime.timezone.utc), verbose_name='تاریخ افزودن'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='date_modify',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر'),
        ),
    ]