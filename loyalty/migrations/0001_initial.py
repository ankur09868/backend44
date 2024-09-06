# Generated by Django 4.1 on 2024-09-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loyalty",
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
                ("entity_id", models.PositiveIntegerField()),
                (
                    "loyalty_program",
                    models.CharField(
                        choices=[
                            ("Promo Code", "Promo Code"),
                            ("Loyalty Cards", "Loyalty Cards"),
                            ("Fidelity Cards", "Fidelity Cards"),
                            ("Promotional Program", "Promotional Program"),
                            ("Coupons", "Coupons"),
                            ("2+1 Free", "2+1 Free"),
                            ("Next Order Coupons", "Next Order Coupons"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "US Dollar"),
                            ("EUR", "Euro"),
                            ("GBP", "British Pound"),
                            ("JPY", "Japanese Yen"),
                            ("INR", "Indian Rupee"),
                        ],
                        default="INR",
                        max_length=3,
                    ),
                ),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "contacts",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacts.contact",
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
    ]
