from cateringandevent.models import Catering_Event
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from services.api.filters import Catering_EventFilter
from rest_framework import serializers
from business.models import Business
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import ForeignKey
from copy import copy
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from profiles.models import  Profile


class Catering_EventList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Catering_Event.objects.all()
    serializer_class = Catering_EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catering_EventFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


class Catering_EventByCategory(generics.ListAPIView):
    serializer_class = Catering_EventSerializer
    permission_classes = [AllowAny]
    queryset = Catering_Event.objects.all()
    serializer_class = Catering_EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catering_EventFilter

    def get_queryset(self):
        category = self.kwargs['category']
        return Catering_Event.objects.filter(category__name=category)
    


class Catering_EventBySubcategory(generics.ListAPIView):
    serializer_class = Catering_EventSerializer
    permission_classes = [AllowAny]
    queryset = Catering_Event.objects.all()
    serializer_class = Catering_EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catering_EventFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        return Catering_Event.objects.filter(category__name=category, subcategory__name=subcategory)


class Catering_EventByType(generics.ListAPIView):
    serializer_class = Catering_EventSerializer
    permission_classes = [AllowAny]
    queryset = Catering_Event.objects.all()
    serializer_class = Catering_EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Catering_EventFilter

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        return Catering_Event.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name)


# ... other import statements ...


# ... other code ...

class Catering_EventDetailView(generics.ListAPIView):
    serializer_class = Catering_EventSerializer
    permission_classes = [AllowAny]
    serializer_class = Catering_EventSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        subcategory = self.kwargs['subcategory']
        type_name = self.kwargs['type']
        service_serial=self.kwargs['service_serial']
        return Catering_Event.objects.filter(category__name=category, subcategory__name=subcategory, type__name=type_name,service_serial=service_serial)


# ... other

class CreateCatering_EventAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        profile = Profile.objects.get(user=user.id)
        business = Business.objects.get(owner=profile.id)

        # Get the foreign key fields from the Catering_Event model
        foreign_key_fields = []
        file_fields = []

        for field in Catering_Event._meta.fields:
            if isinstance(field, ForeignKey):
                foreign_key_fields.append(field.name)
            if 'image' in field.name:
                file_fields.append(field.name)

        # Create a mutable copy of request.data
        mutable_data = request.data.copy()

        # Replace foreign key fields with their respective IDs
        for field_name in foreign_key_fields:
            field_value = mutable_data.get(field_name)
            if field_value:
                fk_model = Catering_Event._meta.get_field(field_name).related_model
                try:
                    fk_object = fk_model.objects.filter(name=field_value).first()  # Get the first matching object
                    if fk_object:
                        mutable_data[field_name] = fk_object.pk
                    else:
                        return Response({field_name: 'Field value does not exist'}, status=400)
                except fk_model.DoesNotExist:
                    return Response({field_name: 'Field value does not exist'}, status=400)

        # Pass the modified data to the serializer
        serializer = Catering_EventCreateSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save(owner=business)
            return Response({'detail':'Product  created!!'}, status=200)
        return Response(serializer.errors, status=400)


