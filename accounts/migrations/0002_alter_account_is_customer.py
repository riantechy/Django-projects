# Generated by Django 4.1.7 on 2023-07-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
    ]