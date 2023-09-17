from groceries.models import Grocery
from rest_framework import generics
from .serializers import GrocerySerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from products.api.filters import GroceryFilter
from rest_framework import serializers
from business.models import Business
from rest_framework_simplejwt.authentication import JWTAuthentication

class GroceryList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroceryFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


class GroceryByCategory(generics.ListAPIView):
    serializer_class = GrocerySerializer
    permission_classes = [AllowAny]
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroceryFilter

    def get_queryset(self):
        category = self.kwargs['category']
        return Grocery.objects.filter(category__name=category)
    


class GroceryBySubcategory(generics.ListAPIView):
    serializer_class = GrocerySerializer
    permission_classes = [AllowAny]
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroceryFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        return Grocery.objects.filter(category__name=category, subcategory__name=subcategory)


class GroceryByType(generics.ListAPIView):
    serializer_class = GrocerySerializer
    permission_classes = [AllowAny]
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroceryFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        return Grocery.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name)


# ... other import statements ...


# ... other code ...

class GroceryDetailView(generics.ListAPIView):
    serializer_class = GrocerySerializer
    permission_classes = [AllowAny]
    serializer_class = GrocerySerializer

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        product_serial=self.kwargs['product_serial']
        return Grocery.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name,product_serial=product_serial)


# ... other code ...



from django.db.models import ForeignKey
from copy import copy
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import *
from  profiles.models import Profile

class CreateGroceryAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        profile = Profile.objects.get(user=user.id)
        business = Business.objects.get(owner=profile.id)
        

        # Get the foreign key fields from the Grocery model
        foreign_key_fields = []
        file_fields = []

        for field in Grocery._meta.fields:
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
                fk_model = Grocery._meta.get_field(field_name).related_model
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
      
        serializer = GroceryCreateSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save(owner=business)
            return Response({'detail':'Product  created!!'}, status=200)
        return Response(serializer.errors, status=400)
