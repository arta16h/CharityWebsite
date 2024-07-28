# Generated by Django 5.0.6 on 2024-07-28 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_documentcategory_document_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator('09(\\d{9})$')], verbose_name='شماره موکب')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('credit', models.CharField(blank=True, max_length=16, null=True, verbose_name='شماره کارت')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='آدرس')),
                ('igurl', models.URLField(blank=True, max_length=255, null=True, verbose_name='لینک اینستاگرام')),
                ('telurl', models.URLField(blank=True, max_length=255, null=True, verbose_name='لینک تلگرام')),
                ('eturl', models.URLField(blank=True, max_length=255, null=True, verbose_name='لینک ایتا')),
                ('homeh1', models.CharField(blank=True, max_length=255, null=True, verbose_name='تیتر اول صفحه اصلی')),
                ('homeh2', models.CharField(blank=True, max_length=255, null=True, verbose_name='تیتر دوم صفحه اصلی')),
                ('homeh3', models.CharField(blank=True, max_length=255, null=True, verbose_name='متن اول صفحه اصلی')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='لوگو')),
                ('home', models.ImageField(blank=True, null=True, upload_to='home/', verbose_name='عکس صفحه اصلی')),
                ('footerabout', models.CharField(blank=True, max_length=255, null=True, verbose_name='اطلاعات فوتر')),
            ],
            options={
                'verbose_name': 'اطلاعات',
                'verbose_name_plural': 'اطلاعات',
            },
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'مدرک', 'verbose_name_plural': 'مدارک'},
        ),
        migrations.AlterModelOptions(
            name='documentcategory',
            options={'verbose_name': 'نوع مدرک', 'verbose_name_plural': 'انواع مدارک'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'عضو', 'verbose_name_plural': 'اعضا'},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name': 'داوطلب', 'verbose_name_plural': 'داوطلب ها'},
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/', verbose_name='مدارک'),
        ),
    ]
