from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny ,IsAuthenticated
from products.models import BaseProduct
from services.models import BaseService
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
from django.apps import apps
from beauty.api.serializers import *
from cateringandevent.api.serializers import *
from cleaning.api.serializers import *
from computerandit.api.serializers import *
from mechanic.api.serializers import *
from transportation.api.serializers import *
from services.api.filters import *

from beauty.models import *
from cateringandevent.models import *
from cleaning.models import *
from computerandit.models import *
from mechanic.models import *
from transportation.models import *
from services.api.filters import *


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def app_list(request):
    # Get all app configs
    apps_to_include = settings.ECOMMERCE_SERVICE_APPS

    # Filter out app configs for apps to exclude
    apps_to_exclude = ['accounts', 'profiles', 'locations', 'order', 'products']
    app_names = [app for app in apps_to_include if app not in apps_to_exclude]

    # Check if the app has any products
    def has_products(app_name):
        try:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseProduct) and model.objects.exists():
                    return True
        except LookupError:
            pass
        return False

    # Filter out app names without products
    app_names_with_products = list(filter(has_products, app_names))

    # Return the list of app names in the response
    return Response(app_names_with_products, status=status.HTTP_200_OK)






class AllServicesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        beauty = BeautyFilter(data={'search': search}, queryset=Beauty.objects.all()).qs
        cateringandevent = Catering_EventFilter(data={'search': search}, queryset=Catering_Event.objects.all()).qs
        cleaning = CleaningFilter(data={'search': search}, queryset=Cleaning.objects.all()).qs
        computerandit = Computer_ItFilter(data={'search': search},queryset=Computer_It.objects.all()).qs
        mechanic = MechanicFilter(data={'search': search},queryset=Mechanic.objects.all()).qs
        transaportation = TransportFilter(data={'search': search},queryset=Transport.objects.all()).qs
        
       # Create instances of multiple serializers
        beauty_serializer = BeautySerializer(beauty, many=True, context={'request': request})
        cateringandevent_serializer = Catering_EventSerializer(cateringandevent, many=True, context={'request': request})
        cleaning_serializer = CleaningSerializer(cleaning, many=True, context={'request': request})
        computerandit_serializer = Computer_ItSerializer(computerandit, many=True, context={'request': request})
        mechanic_serializer = MechanicSerializer(mechanic, many=True, context={'request': request})
        transaportation_serializer = TransportSerializer(transaportation, many=True, context={'request': request})

        # Concatenate the serialized data from each serializer into a single list
        data = (
            beauty_serializer.data +
            cateringandevent_serializer.data +
            cleaning_serializer.data +
            computerandit_serializer.data +
            mechanic_serializer.data +
            transaportation_serializer.data 
        )


        return Response(data, status=status.HTTP_200_OK)
    
class AllServicesAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        beauty = BeautyFilter(data={'search': search}, queryset=Beauty.objects.all()).qs
        cateringandevent = Catering_EventFilter(data={'search': search}, queryset=Catering_Event.objects.all()).qs
        cleaning = CleaningFilter(data={'search': search}, queryset=Cleaning.objects.all()).qs
        computerandit = Computer_ItFilter(data={'search': search},queryset=Computer_It.objects.all()).qs
        mechanic = MechanicFilter(data={'search': search},queryset=Mechanic.objects.all()).qs
        transaportation = TransportFilter(data={'search': search},queryset=Transport.objects.all()).qs
        
       # Create instances of multiple serializers
        beauty_serializer = BeautySerializer(beauty, many=True, context={'request': request})
        cateringandevent_serializer = Catering_EventSerializer(cateringandevent, many=True, context={'request': request})
        cleaning_serializer = CleaningSerializer(cleaning, many=True, context={'request': request})
        computerandit_serializer = Computer_ItSerializer(computerandit, many=True, context={'request': request})
        mechanic_serializer = MechanicSerializer(mechanic, many=True, context={'request': request})
        transaportation_serializer = TransportSerializer(transaportation, many=True, context={'request': request})

        # Concatenate the serialized data from each serializer into a single list
        data = (
            beauty_serializer.data +
            cateringandevent_serializer.data +
            cleaning_serializer.data +
            computerandit_serializer.data +
            mechanic_serializer.data +
            transaportation_serializer.data 
        )


        return Response(data, status=status.HTTP_200_OK)