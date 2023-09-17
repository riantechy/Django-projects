from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import AppRegistryNotReady
from django.db import models
from django.db.models import Q
from accounts.models import Account
from business.models import Business
from products.models import BaseProduct
from services.models import BaseService
from profiles.models import Profile
from locations.models import Locality

class OrderStatus(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


def get_product_q_objects():
    try:
        models = apps.get_models(include_auto_created=False)
        model_names = [model._meta.model_name for model in models if issubclass(model, BaseProduct)]
        return Q(**{f"model__in": model_names})
    except AppRegistryNotReady:
        return Q()


def get_service_q_objects():
    try:
        models = apps.get_models(include_auto_created=False)
        model_names = [model._meta.model_name for model in models if issubclass(model, BaseService)]
        return Q(**{f"model__in": model_names})
    except AppRegistryNotReady:
        return Q()


class Product_Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_serial = models.CharField(max_length=60)
    product_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=get_product_q_objects,
        related_name='product_orders'
    )
    product_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_type', 'product_id')
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality ,on_delete=models.CASCADE,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def product_total_orders(self):
        try:
            count = Product_Order.objects.filter(customer=self.customer).count()
            return count
        except self.DoesNotExist:
            return 0

        


    @property
    def customer_name(self):
        try:
            profile = Profile.objects.get(user=self.customer)
            return profile.first_name
        except Profile.DoesNotExist:
            return None

    @property
    def customer_phone(self):        
        return self.customer.phone_number

    @property
    def business_name(self):
        return self.business.name

    @property
    def business_phonenumber(self):
        return self.business.phone_number

    @property
    def product_title(self):
        if self.product:
            product_model = self.product_type.model_class()
            try:
                product = product_model.objects.get(id=self.product_id)
                if isinstance(product, BaseProduct):
                    title = product.title
                elif isinstance(product, BaseService):
                    title = product.title
                else:
                    title = None
                return title
            except product_model.DoesNotExist:
                return None
        else:
            return None

    @property
    def product_image(self):
        product_model = self.product_type.model_class()
        try:
            product = product_model.objects.get(id=self.product_id)
            if isinstance(product, BaseProduct):
                image_url = product.image1
            elif isinstance(product, BaseService):
                image_url = product.image1
            else:
                image_url = None
            return image_url
        except product_model.DoesNotExist:
            return None


class Service_Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    service_serial = models.CharField(max_length=60)
    service_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=get_service_q_objects,
        related_name='service_orders'
    )
    service_id = models.PositiveIntegerField()
    service = GenericForeignKey('service_type', 'service_id')

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def service_total_orders(self):
        try:
            count = Product_Order.objects.filter(customer=self.customer).count()
            return count
        except self.DoesNotExist:
            return 0      


    @property
    def customer_name(self):
        try:
            profile = Profile.objects.get(user=self.customer)
            return profile.first_name
        except Profile.DoesNotExist:
            return None

    @property
    def customer_phone(self):        
        return self.customer.phone_number

    @property
    def business_name(self):
        return self.business.name

    @property
    def business_phonenumber(self):
        return self.business.phone_number

    @property
    def product_title(self):
        if self.product:
            product_model = self.product_type.model_class()
            try:
                product = product_model.objects.get(id=self.product_id)
                if isinstance(product, BaseProduct):
                    title = product.title
                elif isinstance(product, BaseService):
                    title = product.title
                else:
                    title = None
                return title
            except product_model.DoesNotExist:
                return None
        else:
            return None

    @property
    def product_image(self):
        product_model = self.product_type.model_class()
        try:
            product = product_model.objects.get(id=self.product_id)
            if isinstance(product, BaseProduct):
                image_url = product.image1
            elif isinstance(product, BaseService):
                image_url = product.image1
            else:
                image_url = None
            return image_url
        except product_model.DoesNotExist:
            return None

