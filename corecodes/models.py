from django.db import models
from django.utils import timezone

class FrontEndLogo(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Homepage(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TermsandConditions(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    heading_count = models.DecimalField(decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
