# Generated by Django 4.1 on 2024-06-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tenant",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("organization", models.CharField(max_length=100)),
                ("db_user", models.CharField(max_length=100)),
                ("db_user_password", models.CharField(max_length=100)),
            ],
        ),
    ]