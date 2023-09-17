from appliances.models import *
from rest_framework import generics,status
from .serializers import ApplianceSerializer,ApplianceCreateSerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from products.api.filters import ApplianceFilter
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from profiles.models import Profile
from business.models import Business
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class ApplianceList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplianceFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context



class AppliancesByCategory(generics.ListAPIView):
    serializer_class = ApplianceSerializer
    permission_classes = [AllowAny]
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplianceFilter

    def get_queryset(self):
        category = self.kwargs['category']
        return Appliance.objects.filter(category__name=category)
    


class AppliancesBySubcategory(generics.ListAPIView):
    serializer_class = ApplianceSerializer
    permission_classes = [AllowAny]
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplianceFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        return Appliance.objects.filter(category__name=category, subcategory__name=subcategory)


class AppliancesByType(generics.ListAPIView):
    serializer_class = ApplianceSerializer
    permission_classes = [AllowAny]
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplianceFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        return Appliance.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name)



class ApplianceDetailView(generics.ListAPIView):
    serializer_class = ApplianceSerializer
    permission_classes = [AllowAny]
    serializer_class = ApplianceSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        product_serial=self.kwargs['product_serial']
        return Appliance.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name,product_serial=product_serial)



class ApplianceEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplianceCreateSerializer
    permission_classes = [AllowAny]
    queryset = Appliance.objects.all()

    def get_object(self):
        # Retrieve the Appliance object based on the provided ID
        appliance_id = self.kwargs['product_serial']
        return self.queryset.get(product_serial=appliance_id)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        # Delete the Appliance object
        instance.delete()




from django.db.models import ForeignKey
from copy import copy
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import *
from  profiles.models import Profile

class CreateApplianceAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        profile = Profile.objects.get(user=user.id)
        business = Business.objects.get(owner=profile.id)
        

        # Get the foreign key fields from the Appliance model
        foreign_key_fields = []
        file_fields = []

        for field in Appliance._meta.fields:
            if isinstance(field, ForeignKey):
                foreign_key_fields.append(field.name)
            if 'image' in field.name:
                file_fields.append(field.name)

        # Create a mutable copy of request.data
        mutable_data = request.data.copy()
        # print(mutable_data)
        # print(foreign_key_fields)

        # Replace foreign key fields with their respective IDs
        for field_name in foreign_key_fields:
            field_value = mutable_data.get(field_name)
            if field_value:
                fk_model = Appliance._meta.get_field(field_name).related_model
                try:
                    fk_object = fk_model.objects.filter(name=field_value).first()  # Get the first matching object
                    print(field_name,fk_object,fk_object.pk)
                    if fk_object:
                        mutable_data[field_name] = fk_object.pk
                    else:
                        return Response({field_name: 'Field value does not exist'}, status=400)
                except fk_model.DoesNotExist:
                    return Response({field_name: 'Field value does not exist'}, status=400)

        # Pass the modified data to the serializer
        print(mutable_data)
      
        serializer = ApplianceCreateSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save(owner=business)
            return Response({'detail':'Product  created!!'}, status=200)
        return Response(serializer.errors, status=400)
