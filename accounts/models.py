from typing import Any
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile
from django_countries.fields import CountryField
from phonenumbers.phonenumberutil import NumberParseException
from profiles.models import Profile
import phonenumbers

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=32,unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    country_code = CountryField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)   
    is_merchant = models.BooleanField(default=False)  
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','username']

    def __str__(self):
        return f'{self.email} {self.username}'

    def normalize_phone_number(self):
        try:
            phone_number = phonenumbers.parse(self.phone_number, None)
            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError('Invalid phone number')
            return phone_number
        except NumberParseException:
            raise ValueError('Unable to parse phone number')
    
@receiver(post_save, sender=Account)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class ActivationCode(models.Model):
    email = models.EmailField(max_length=64)
    code = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
      
    class Meta:
        verbose_name = 'Activation Code'
        verbose_name_plural = 'Activation Codes'

    def __str__(self):
        return self.code


class CustomerManager(MyUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_customer=True)

class AdminManager(MyUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)

class SupportManager(MyUserManager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_admin=True)

    
class MerchantManager(MyUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_merchant=True)

class Customer(Account):
    objects = CustomerManager()

    class Meta:
        proxy = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    @property
    def customer_name(self):
        try:
            profile = Profile.objects.get(user=self)
            return profile.first_name
        except Profile.DoesNotExist:
            return None
        
    def save(self, *args, **kwargs):
        self.is_customer = True
        self.is_admin = self.is_admin
        self.is_support = self.is_support
        self.is_merchant = self.is_merchant

        super().save(*args, **kwargs)

class Merchant(Account):
    objects = MerchantManager()

    class Meta:
        proxy = True
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'
    @property
    def merchant_name(self):
        try:
            profile = Profile.objects.get(user=self)
            return profile.first_name
        except Profile.DoesNotExist:
            return None

    def save(self, *args, **kwargs):
        self.is_customer = self.is_customer
        self.is_admin = self.is_admin
        self.is_support = self.is_support
        self.is_merchant = True

        super().save(*args, **kwargs)

class Admin(Account):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def save(self, *args, **kwargs):
        self.is_customer = False
        self.is_admin = True
        self.is_support = self.is_support
        self.is_merchant = False

        super().save(*args, **kwargs)

class Support(Account):
    objects = SupportManager()

    class Meta:
        proxy = True
        verbose_name = 'Technical Support'
        verbose_name_plural = 'Technical Support'

   
