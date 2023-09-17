# Generated by Django 4.1.7 on 2023-06-27 10:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_Service_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Other_Service_Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ManyToManyField(to='otherservices.other_service_category')),
            ],
        ),
        migrations.CreateModel(
            name='Other_Service_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subcategory', models.ManyToManyField(to='otherservices.other_service_sub_category')),
            ],
        ),
        migrations.CreateModel(
            name='Other_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image1', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=False, quality=97, scale=None, size=[600, 600], upload_to=services.models.upload_location)),
                ('image2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=services.models.upload_location)),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=services.models.upload_location)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency', models.CharField(default='KES', max_length=5)),
                ('is_mobile', models.BooleanField(default=False)),
                ('negotiable', models.BooleanField(default=False)),
                ('sponsored', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('service_serial', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_service_items', to='otherservices.other_service_category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.region')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_service_subitems', to='otherservices.other_service_sub_category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_service_subtypeitems', to='otherservices.other_service_type')),
            ],
            options={
                'verbose_name': 'Other_Service service',
                'verbose_name_plural': 'Other_Service services',
            },
        ),
    ]
