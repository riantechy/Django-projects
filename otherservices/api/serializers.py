from rest_framework import serializers
from business.models import Business
from locations.models import Locality
from otherservices.models import *
from locations.api.serializers import LocalitySerializer
class GenericNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']

    def __init__(self, model, *args, **kwargs):
        self.Meta.model = model
        super().__init__(*args, **kwargs)



class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business  # Replace with your BUSINESS MODEL
        fields = ['name', 'phone_number']  # Replace with the name and phone number fields in your Business model


class Other_ServiceSerializer(serializers.ModelSerializer):
    category = GenericNameSerializer(Other_Service_Category)
    subcategory = GenericNameSerializer(Other_Service_Sub_Category)
    type = GenericNameSerializer(Other_Service_Type)
    locality=LocalitySerializer() # Add this field to the serializer
    app_name = serializers.SerializerMethodField()
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = Other_Service
        exclude = ["owner", "id", "sponsored", "featured", "new"]
        read_only_fields = ['owner']

    def get_app_name(self, obj):
        return obj.__class__._meta.app_label

    def get_owner_info(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            owner_serializer = OwnerSerializer(obj.owner)
            return owner_serializer.data
        return None

class Other_ServiceCreateSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Other_Service
        exclude = ["owner", "id", "created", "updated", "slug", "currency", "product_serial",
                   "sponsored", "featured", "new", "most_sold", "out_of_stock"]

        
