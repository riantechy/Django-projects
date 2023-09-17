from rest_framework import serializers
from healthandbeauty.models import *
from business.models import Business
from appliances.models import *
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

class Health_BeautySerializer(serializers.ModelSerializer):
    category = GenericNameSerializer(Health_Beauty_Category)
    subcategory = GenericNameSerializer(Health_Beauty_Sub_Category)
    type = GenericNameSerializer(Health_Beauty_Type)
    color = GenericNameSerializer(Health_Beauty_Color)
    size = GenericNameSerializer(Health_Beauty_Size)
    material = GenericNameSerializer(Health_Beauty_Material)
    brand = GenericNameSerializer(Health_Beauty_Brand)
    locality=LocalitySerializer() # Add this field to the serializer
    per= GenericNameSerializer(Per)
    packaging= GenericNameSerializer(Package)
    app_name = serializers.SerializerMethodField()
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = Health_Beauty
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



class Health_BeautyCreateSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Health_Beauty
        exclude = ["owner", "id", "created", "updated", "slug", "currency", "product_serial",
                   "sponsored", "featured", "new", "most_sold", "out_of_stock"]

        
