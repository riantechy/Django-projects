# Generated by Django 2.2.12 on 2022-07-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
