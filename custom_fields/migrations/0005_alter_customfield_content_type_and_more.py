# Generated by Django 4.1 on 2024-08-13 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('custom_fields', '0004_remove_customfield_entity_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_fields', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
