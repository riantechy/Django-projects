# Generated by Django 4.1.7 on 2023-06-27 12:22

import business.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_permit',
            field=models.FileField(blank=True, null=True, upload_to=business.models.upload_location, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='business',
            name='id_attachment',
            field=models.FileField(blank=True, null=True, upload_to=None, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='business',
            name='kra_pin_attachment',
            field=models.FileField(blank=True, null=True, upload_to=None, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
