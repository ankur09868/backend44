# Generated by Django 4.1 on 2024-05-30 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tenant", "0002_tenant_organization"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vendor_owner", models.CharField(max_length=100)),
                ("vendor_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("website", models.URLField(blank=True)),
                ("category", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tenant.tenant"
                    ),
                ),
            ],
        ),
    ]
