from rest_framework import serializers
from phoneandtablet.models import *
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


class Phone_TabletSerializer(serializers.ModelSerializer):
    category = GenericNameSerializer(Phone_Tablet_Category)
    subcategory = GenericNameSerializer(Phone_Tablet_Sub_Category)
    type = GenericNameSerializer(Phone_Tablet_Type)
    color = GenericNameSerializer(Phone_Tablet_Color)
    size = GenericNameSerializer(Phone_Tablet_Size)
    material = GenericNameSerializer(Phone_Tablet_Material)
    brand = GenericNameSerializer(Phone_Tablet_Brand)
    condition = GenericNameSerializer(Phone_Tablet_Condition)
    locality=LocalitySerializer() # Add this field to the serializer
    per= GenericNameSerializer(Per)
    packaging= GenericNameSerializer(Package)
    app_name = serializers.SerializerMethodField()
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = Phone_Tablet
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


class Phone_TabletCreateSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Phone_Tablet
        exclude = ["owner", "id", "created", "updated", "slug", "currency", "product_serial",
                   "sponsored", "featured", "new", "most_sold", "out_of_stock"]

        
