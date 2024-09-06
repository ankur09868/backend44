# Generated by Django 4.1 on 2024-09-06 15:22

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallCampaign",
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
                ("caller_id", models.CharField(max_length=255)),
                ("call_script", models.TextField(blank=True, null=True)),
                ("number_of_calls", models.IntegerField(default=0)),
                ("call_duration", models.DurationField(blank=True, null=True)),
                (
                    "call_outcome",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("successful_calls", models.IntegerField(default=0)),
                ("failed_calls", models.IntegerField(default=0)),
                (
                    "engagement_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Call Campaign",
                "verbose_name_plural": "Call Campaigns",
            },
        ),
        migrations.CreateModel(
            name="Campaign",
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
                ("campaign_name", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "expected_revenue",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("actual_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("numbers_sent", models.IntegerField()),
                (
                    "type",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("Email", "Email"),
                                ("CALL", "CALL"),
                                ("WHATSAPP", "WHATSAPP"),
                                ("INSTAGRAM", "INSTAGRAM"),
                            ],
                            max_length=50,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Active", "Active"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                        ],
                        max_length=50,
                    ),
                ),
                ("budgeted_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "expected_response",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="WhatsAppCampaign",
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
                ("broadcast_message", models.TextField(blank=True, null=True)),
                ("chatbot_enabled", models.BooleanField(default=False)),
                ("chatbot_script", models.TextField(blank=True, null=True)),
                ("ai_integration", models.BooleanField(default=False)),
                ("ai_features", models.TextField(blank=True, null=True)),
                (
                    "target_audience",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("message_template", models.TextField(blank=True, null=True)),
                ("number_of_recipients", models.IntegerField(default=0)),
                ("scheduling_time", models.DateTimeField(blank=True, null=True)),
                (
                    "engagement_goal",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "actual_engagement",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "campaign",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="whatsapp_campaign",
                        to="campaign.campaign",
                    ),
                ),
            ],
            options={
                "verbose_name": "WhatsApp Campaign",
                "verbose_name_plural": "WhatsApp Campaigns",
            },
        ),
        migrations.CreateModel(
            name="InstagramCampaign",
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
                (
                    "campaign_tone",
                    models.CharField(
                        choices=[
                            ("Informative", "Informative"),
                            ("Promotional", "Promotional"),
                            ("Engaging", "Engaging"),
                            ("Storytelling", "Storytelling"),
                        ],
                        default="Promotional",
                        max_length=50,
                    ),
                ),
                ("number_of_posts", models.IntegerField(default=1)),
                ("target_hashtags", models.TextField(blank=True, null=True)),
                ("duration", models.DurationField(blank=True, null=True)),
                (
                    "audience_targeting",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "call_to_action",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "engagement_goal",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "actual_engagement",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "campaign",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instagram_campaign",
                        to="campaign.campaign",
                    ),
                ),
            ],
            options={
                "verbose_name": "Instagram Campaign",
                "verbose_name_plural": "Instagram Campaigns",
            },
        ),
        migrations.CreateModel(
            name="EmailCampaign",
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
                ("subject_line", models.CharField(max_length=255)),
                ("email_body", models.TextField()),
                ("sender_email", models.EmailField(max_length=254)),
                ("recipient_list", models.TextField(blank=True, null=True)),
                ("scheduled_time", models.DateTimeField(blank=True, null=True)),
                ("email_template", models.TextField(blank=True, null=True)),
                ("emails_sent", models.IntegerField(default=0)),
                ("emails_opened", models.IntegerField(default=0)),
                ("clicks", models.IntegerField(default=0)),
                ("bounces", models.IntegerField(default=0)),
                ("unsubscribes", models.IntegerField(default=0)),
                (
                    "engagement_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                ("email_html", models.TextField(blank=True, null=True)),
                (
                    "campaign",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email_campaign",
                        to="campaign.campaign",
                    ),
                ),
            ],
            options={
                "verbose_name": "Email Campaign",
                "verbose_name_plural": "Email Campaigns",
            },
        ),
    ]
