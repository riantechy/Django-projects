from rest_framework import serializers
from computersandaccessories.models import *
from business.models import Business
from locations.models import Locality
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

class ComputingSerializer(serializers.ModelSerializer):
    category = GenericNameSerializer(Computing_Category)
    subcategory = GenericNameSerializer(Computing_Sub_Category)
    type = GenericNameSerializer(Computing_Type)
    color = GenericNameSerializer(Computing_Color)
    size = GenericNameSerializer(Computing_Size)
    material = GenericNameSerializer(Computing_Material)
    brand = GenericNameSerializer(Computing_Brand)
    condition = GenericNameSerializer(Computing_Condition)
    per= GenericNameSerializer(Per)
    packaging= GenericNameSerializer(Package)
    locality=LocalitySerializer() # Add this field to the serializer
    app_name = serializers.SerializerMethodField()
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = Computing
        exclude = ["owner", "id", "sponsored", "featured", "new", "most_sold", "out_of_stock"]
        read_only_fields = ['owner']

    def get_app_name(self, obj):
        return obj.__class__._meta.app_label

    def get_owner_info(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            owner_serializer = OwnerSerializer(obj.owner)
            return owner_serializer.data
        return None


class ComputingCreateSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Computing
        exclude = ["owner", "id", "created", "updated", "slug", "currency", "product_serial",
                   "sponsored", "featured", "new", "most_sold", "out_of_stock"]

        
