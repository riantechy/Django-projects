# Generated by Django 4.1.7 on 2023-09-17 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_locality_remove_region_county_and_more'),
        ('fashion', '0002_remove_fashion_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashion',
            name='locality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.locality'),
        ),
    ]