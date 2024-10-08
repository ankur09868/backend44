# Generated by Django 4.1 on 2024-09-26 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('analytics', '0002_faissindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.BigIntegerField()),
                ('doc_name', models.CharField(max_length=100)),
                ('data', models.JSONField()),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant')),
            ],
        ),
    ]