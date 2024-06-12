# Generated by Django 4.1 on 2024-06-11 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('account', 'Account'), ('calls', 'Calls'), ('lead', 'Lead'), ('interaction', 'Interaction')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('value', models.TextField(blank=True, null=True)),
                ('field_type', models.CharField(choices=[('char', 'CharField'), ('text', 'TextField'), ('int', 'IntegerField'), ('float', 'FloatField'), ('bool', 'BooleanField'), ('date', 'DateField'), ('datetime', 'DateTimeField'), ('email', 'EmailField'), ('url', 'URLField')], max_length=20)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
