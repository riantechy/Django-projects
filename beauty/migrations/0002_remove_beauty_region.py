# Generated by Django 4.1.7 on 2023-09-17 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beauty',
            name='region',
        ),
    ]
