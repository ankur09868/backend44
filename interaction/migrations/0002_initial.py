# Generated by Django 4.1 on 2024-09-06 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("interaction", "0001_initial"),
        ("tenant", "0001_initial"),
        ("contacts", "0002_initial"),
    ]

   