from rest_framework import serializers
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ["owner","id","ceritificate_of_registration"]
        read_only_fields=["is_verified","is_top_rated","created" ,"updated",]       
        read_only_fields = ['owner']

class BusinessUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ["owner","id","id_attachment","business_permit","kra_pin_attachment","ceritificate_of_registration","social_media_links", "founded_in","website"]
        read_only_fields=["is_verified","is_top_rated","created" ,"updated",]        
        read_only_fields = ['owner']



