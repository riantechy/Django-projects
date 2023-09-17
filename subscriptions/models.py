from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Subscription(models.Model):
    business = models.OneToOneField('business.Business', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    is_trial = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Check if it's a new subscription
        if not self.pk:
            # Set the end date based on the start date
            self.end_date = self.start_date + timedelta(days=120)  # Assuming a 30-day trial period
        
        super().save(*args, **kwargs)

    def is_active(self):
        current_date = timezone.now().date()
        return self.end_date is None or current_date <= self.end_date

    def is_trial_expired(self):
        current_date = timezone.now().date()
        return self.is_trial and self.end_date and current_date > self.end_date

    def activate_subscription(self):
        self.is_trial = False
        self.save()

    def extend_subscription(self, days):
        if self.end_date:
            self.end_date += timedelta(days=days)
        else:
            self.end_date = timezone.now().date() + timedelta(days=days)
        self.save()
