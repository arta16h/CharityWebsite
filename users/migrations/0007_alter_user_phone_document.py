# Generated by Django 5.0.6 on 2024-07-17 07:40

import django.core.validators
import django.db.models.deletion
import utils.file_path_creator
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_city_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=14, unique=True, validators=[django.core.validators.RegexValidator('09(\\d{9})$')], verbose_name='شماره تماس'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام فایل')),
                ('file', models.FileField(upload_to=utils.file_path_creator.make_image_path, verbose_name='مدارک')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='توضیحات')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]