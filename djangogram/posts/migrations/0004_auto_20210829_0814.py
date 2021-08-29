# Generated by Django 3.1.13 on 2021-08-29 08:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20210103_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_likes',
            field=models.ManyToManyField(blank=True, related_name='post_image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
