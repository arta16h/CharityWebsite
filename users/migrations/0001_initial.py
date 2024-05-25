# Generated by Django 5.0.6 on 2024-05-25 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('nc', models.IntegerField()),
                ('gender', models.CharField(choices=[(1, 'مونث'), (2, 'مذکر')], max_length=10)),
                ('marital_status', models.CharField(choices=[(1, 'مجرد'), (2, 'متاهل')], max_length=10)),
                ('phone', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator('09(\\d{9})$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('major', models.CharField(max_length=100)),
                ('education', models.CharField(choices=[(1, 'دیپلم'), (2, 'کاردانی'), (3, 'کارشناسی'), (4, 'کارشناسی ارشد'), (5, 'دکتری')], max_length=25)),
                ('city', models.CharField(max_length=100)),
                ('abilities', models.CharField(choices=[('piping', 'لوله کشی'), ('building', 'بنا'), ('welder', 'جوشکار'), ('electrician', 'برقکار'), ('plaster', 'گچ کار'), ('facilities', 'تاسیسات'), ('graphist', 'گرافیست'), ('programmer', 'برنامه نویس'), ('photographer', 'عکاس'), ('Cameraman', 'فیلم بردار'), ('editor', 'ویرایشگر'), ('content', 'تولید محتوا'), ('speaker', 'گوینده'), ('kindergarten', 'مهدکودک'), ('translator', 'مترجم عربی'), ('PA', 'پزشک عمومی'), ('specialist', 'پزشک متخصص'), ('psychologist', 'روانشناس'), ('consult', 'مشاوره'), ('dentist', 'دندان پزشک'), ('pharmacist', 'داروساز'), ('nurse', 'پرستار'), ('executive', 'پشتیبان اجرایی'), ('cook', 'آشپز'), ('heavy vehicle', 'راننده ماشین سنگین'), ('pickup truck', 'راننده وانت')], max_length=50)),
                ('specialist_info', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='images/users/<django.db.models.fields.CharField>_<django.db.models.fields.CharField>/')),
                ('experience', models.CharField(choices=[(1, 'دارم'), (2, 'ندارم')], max_length=10)),
                ('experience_info', models.TextField()),
            ],
        ),
    ]
