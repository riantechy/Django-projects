from rest_framework import serializers
from orders.models import Product_Order, Service_Order
from locations.api.serializers import Locality

class ProductOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    customer_phone = serializers.SerializerMethodField()
    business_name = serializers.SerializerMethodField()
    business_phonenumber = serializers.SerializerMethodField()
    product_image = serializers.ImageField(use_url=True)  # Use ImageField to handle image media files
    product_title = serializers.SerializerMethodField()

    def get_customer_name(self, instance):
        return instance.customer_name

    def get_customer_phone(self, instance):
        return instance.customer_phone

    def get_business_name(self, instance):
        return instance.business_name

    def get_business_phonenumber(self, instance):
        return instance.business_phonenumber

    def get_product_title(self, instance):
        return instance.product_title

    class Meta:
        model = Product_Order
        exclude = ["id", "customer", "product_type", "business", "product_id"]


class ServiceOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    customer_phone = serializers.SerializerMethodField()
    business_name = serializers.SerializerMethodField()
    business_phonenumber = serializers.SerializerMethodField()
    service_image =  serializers.ImageField(use_url=True)
    service_title = serializers.SerializerMethodField()
    def get_customer_name(self, instance):
        return instance.customer_name

    def get_customer_phone(self, instance):
        return instance.customer_phone

    def get_business_name(self, instance):
        return instance.business_name

    def get_business_phonenumber(self, instance):
        return instance.business_phonenumber


    def get_service_title(self, instance):
        return instance.service_title

    class Meta:
        model = Service_Order
        exclude = ["id" , "customer","service_type" ,"business" ,"service_id"]
