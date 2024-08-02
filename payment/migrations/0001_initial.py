# Generated by Django 5.0.6 on 2024-08-01 17:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('slug', models.SlugField(verbose_name='اسلاگ')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال است')),
                ('image', models.ImageField(blank=True, null=True, upload_to='payment_category_images/', verbose_name='تصویر')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ افزودن')),
                ('date_modify', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')),
            ],
            options={
                'verbose_name': 'دسته پرداخت',
                'verbose_name_plural': 'دسته های پرداخت',
                'db_table': 'payment_category',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='description')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('image', models.ImageField(blank=True, null=True, upload_to='payment_method_images/', verbose_name='image')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modify', models.DateTimeField(auto_now=True, verbose_name='date modify')),
            ],
            options={
                'verbose_name': 'روش پرداخت',
                'verbose_name_plural': 'روش های پرداخت',
                'db_table': 'payment_method',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_trace_id', models.UUIDField(unique=True, verbose_name='payment_id')),
                ('payment_status', models.PositiveSmallIntegerField(choices=[(1, 'در انتظار'), (2, 'در پروسه انجام'), (3, 'در پروسه انجام'), (4, 'در پروسه انجام'), (5, 'در پروسه انجام')], verbose_name='payment_status')),
                ('request_time', models.DateTimeField(verbose_name='request time')),
                ('total_amount', models.PositiveBigIntegerField(verbose_name='total amount')),
                ('pay_id', models.CharField(max_length=30, unique=True, verbose_name='pay id')),
                ('image', models.ImageField(blank=True, null=True, upload_to='payment_images/', verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modify', models.DateTimeField(auto_now=True, verbose_name='date modify')),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='request user')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmethod', verbose_name='payment method')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت ها',
                'db_table': 'payment',
            },
        ),
    ]