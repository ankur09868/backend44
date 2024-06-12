# Generated by Django 4.1 on 2024-06-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64, verbose_name='Name of Account')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('industry', models.CharField(blank=True, max_length=255, null=True, verbose_name='Industry Type')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.CharField(default='Unknown', max_length=100)),
                ('account_type', models.CharField(choices=[('business', 'Business'), ('consumer', 'Consumer')], max_length=10, null=True)),
                ('stage', models.CharField(blank=True, choices=[('Prospect', 'Prospect'), ('Engaged Prospect', 'Engaged Prospect'), ('Lead', 'Lead'), ('Shopping Cart', 'Shopping Cart'), ('Checkout', 'Checkout'), ('New Customer', 'New Customer'), ('Product Setup', 'Product Setup'), ('First Use', 'First Use'), ('Active Customer', 'Active Customer'), ('Support', 'Support'), ('Feedback', 'Feedback'), ('Loyalty Programs', 'Loyalty Programs'), ('Re-Engagement', 'Re-Engagement'), ('Upsell', 'Upsell'), ('Cross-Sell', 'Cross-Sell'), ('Referrals', 'Referrals'), ('At-Risk Customer', 'At-Risk Customer'), ('Lost Customer', 'Lost Customer')], max_length=20, null=True)),
            ],
        ),
    ]
