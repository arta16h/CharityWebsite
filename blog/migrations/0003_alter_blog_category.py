# Generated by Django 5.0.6 on 2024-07-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.category'),
        ),
    ]