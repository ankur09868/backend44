# Generated by Django 4.1 on 2024-09-26 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_initial'),
        ('tenant', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interaction', '0007_calls_call_to_calls_createdby_calls_tenant_and_more'),
    ]

    operations = [
    ]
