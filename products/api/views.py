from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from products.models import BaseProduct
from services.models import BaseService
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
from django.apps import apps
from appliances.api.serializers import ApplianceSerializer
from baby_items.api.serializers import BabyProductSerializer
from computersandaccessories.api.serializers import ComputingSerializer
from fashion.api.serializers import FashionSerializer
from gaming.api.serializers import GamingSerializer
from groceries.api.serializers import GrocerySerializer
from healthandbeauty.api.serializers import Health_BeautySerializer
from homeandoffice.api.serializers import Home_OfficeSerializer
from otherproducts.api.serializers import Other_ProductSerializer
from phoneandtablet.api.serializers import Phone_TabletSerializer
from sporting.api.serializers import Sport_GoodingSerializer
from tvandaudio.api.serializers import Tv_AudioSerializer
from appliances.models import *
from baby_items.models import *
from computersandaccessories.models import *
from fashion.models import *
from gaming.models import *
from groceries.models import *
from healthandbeauty.models import *
from homeandoffice.models import *
from otherproducts.models import *
from phoneandtablet.models import *
from sporting.models import *
from tvandaudio.models import *
from products.api.filters import *
from profiles.models import Profile
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def app_list(request):
    # Get all app configs
    apps_to_include = settings.ECOMMERCE_PRODUCTS_APPS

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


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def sidebar_data_view(request):
    result = {"products": [] , "services": []}

    # Loop over product apps
    for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
        app_data = {"app_name": app_name, "app_count": 0, "categories": []}
        try:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseProduct):
                    # Process categories and subcategories
                    categories = model.objects.order_by('category__name').values_list('category__name', flat=True).distinct()
                    for category in categories:
                        category_data = {'category': category, 'category_count': 0, 'subcategories': []}
                        subcategories = model.objects.filter(category__name=category).order_by('subcategory__name').values_list('subcategory__name', flat=True).distinct()
                        for subcategory in subcategories:
                            subcategory_data = {'subcategory': subcategory, 'subcategory_count': 0, 'types': []}
                            types = model.objects.filter(subcategory__name=subcategory).order_by('type__name').values_list('type__name', flat=True).distinct()
                            for type_name in types:
                                type_count = model.objects.filter(subcategory__name=subcategory, type__name=type_name).count()
                                subcategory_data['types'].append({'type': type_name, 'type_count': type_count})
                                subcategory_data['subcategory_count'] += type_count
                            category_data['subcategories'].append(subcategory_data)
                        category_data['category_count'] = len(category_data['subcategories'])
                        app_data['app_count'] += category_data['category_count']
                        app_data['categories'].append(category_data)
        except LookupError:
            pass

        if app_data['app_count'] > 0:
            result['products'].append(app_data)

    # Loop over service apps
    # Loop over service apps
    for app_name in settings.ECOMMERCE_SERVICE_APPS:
        app_data = {"app_name": app_name, "app_count": 0, "categories": []}
        try:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseService):
                    # Process categories and subcategories
                    categories = model.objects.order_by('category__name').values_list('category__name', flat=True).distinct()
                    for category in categories:
                        category_data = {'category': category, 'category_count': 0, 'subcategories': []}
                        subcategories = model.objects.filter(category__name=category).order_by('subcategory__name').values_list('subcategory__name', flat=True).distinct()
                        for subcategory in subcategories:
                            subcategory_data = {'subcategory': subcategory, 'subcategory_count': 0, 'types': []}
                            types = model.objects.filter(subcategory__name=subcategory).order_by('type__name').values_list('type__name', flat=True).distinct()
                            for type_name in types:
                                type_count = model.objects.filter(subcategory__name=subcategory, type__name=type_name).count()
                                subcategory_data['types'].append({'type': type_name, 'type_count': type_count})
                                subcategory_data['subcategory_count'] += type_count
                            category_data['subcategories'].append(subcategory_data)
                        category_data['category_count'] = len(category_data['subcategories'])
                        app_data['app_count'] += category_data['category_count']
                        app_data['categories'].append(category_data)
        except LookupError:
            pass

        if app_data['app_count'] > 0:
            result['services'].append(app_data)
    return Response(result)





# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([AllowAny])
# def all_products_view(request):
#     result = {"products": [] }

#     # Loop over product apps
#     for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
#         app_data = {"app_name": app_name, "app_count": 0, "categories": []}
#         try:
#             app_config = apps.get_app_config(app_name)
#             for model in app_config.get_models():
#                 if issubclass(model, BaseProduct) and hasattr(model, 'objects'):
#                     # Get the fields of the model
#                     fields = [field.name for field in model._meta.fields]

#                     # Process categories and subcategories
#                     categories = model.objects.order_by('category__name').values_list('category__name', flat=True).distinct()
#                     for category in categories:
#                         category_data = {'category': category, 'category_count': 0, 'subcategories': []}
#                         subcategories = model.objects.filter(category__name=category).order_by('subcategory__name').values_list('subcategory__name', flat=True).distinct()
#                         for subcategory in subcategories:
#                             subcategory_data = {'subcategory': subcategory, 'subcategory_count': 0, 'types': []}
#                             types = model.objects.filter(subcategory__name=subcategory).order_by('type__name').values_list('type__name', flat=True).distinct()
#                             for type_name in types:
#                                 type_count = model.objects.filter(subcategory__name=subcategory, type__name=type_name).count()
#                                 products = model.objects.filter(subcategory__name=subcategory, type__name=type_name)  # get actual products
#                                 products_data = []  # create a list to store product details
#                                 for product in products:
#                                     # create a dictionary to store product details dynamically using the model fields
#                                     for product in products:
#                                         # create a dictionary to store product details dynamically using the model fields
#                                         product_data = {}

#                                         # FILTER
#                                         for field in fields:
#                                             if isinstance(getattr(model, field), ImageField):
#                                                 value = str(request.build_absolute_uri(getattr(product, field).url))  # convert the URL to a string
#                                             else:
#                                                 value = str(getattr(product, field))  # convert other values to strings
#                                             product_data[field] = value
#                                         products_data.append(product_data)  # add product details to the list


#                                 subcategory_data['types'].append({'type': type_name, 'type_count': type_count, 'products': products_data})  # add product details to the subcategory data
#                                 subcategory_data['subcategory_count'] += type_count
#                             category_data['subcategories'].append(subcategory_data)
#                         category_data['category_count'] = len(category_data['subcategories'])
#                         app_data['app_count'] += category_data['category_count']
#                         app_data['categories'].append(category_data)
#         except LookupError:
#             pass

#         if app_data['app_count'] > 0:
#             result['products'].append(app_data)

#     return Response(result)



class AllProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        appliances = ApplianceFilter(data={'search': search}, queryset=Appliance.objects.all()).qs
        baby_products = BabyProductFilter(data={'search': search}, queryset=BabyProduct.objects.all()).qs
        computersandaccessories = ComputingFilter(data={'search': search}, queryset=Computing.objects.all()).qs
        fashion = FashionFilter(data={'search': search},queryset=Fashion.objects.all()).qs
        gaming = GamingFilter(data={'search': search},queryset=Gaming.objects.all()).qs
        groceries = GroceryFilter(data={'search': search},queryset=Grocery.objects.all()).qs
        health_and_beauty = Health_BeautyFilter(data={'search': search},queryset=Health_Beauty.objects.all()).qs
        home_and_office = Home_OfficeFilter(data={'search': search},queryset=Home_Office.objects.all()).qs
        other_products = Other_ProductFilter(data={'search': search},queryset=Other_Product.objects.all()).qs
        phone_and_tablet = Phone_TabletFilter(data={'search': search},queryset=Phone_Tablet.objects.all()).qs
        sporting_goods = Sport_GoodingFilter(data={'search': search},queryset=Sport_Gooding.objects.all()).qs
        tv_and_audio = Tv_AudioFilter(data={'search': search},queryset=Tv_Audio.objects.all()).qs
        appliances_serializer = ApplianceSerializer(appliances, many=True, context={'request': request})
        baby_products_serializer = BabyProductSerializer(baby_products, many=True, context={'request': request})
        computersandaccessories_serializer = ComputingSerializer(computersandaccessories, many=True, context={'request': request})
        fashion_serializer = FashionSerializer(fashion, many=True, context={'request': request})
        gaming_serializer = GamingSerializer(gaming, many=True, context={'request': request})
        groceries_serializer = GrocerySerializer(groceries, many=True, context={'request': request})
        health_and_beauty_serializer = Health_BeautySerializer(health_and_beauty, many=True, context={'request': request})
        home_and_office_serializer = Home_OfficeSerializer(home_and_office, many=True, context={'request': request})
        other_products_serializer = Other_ProductSerializer(other_products, many=True, context={'request': request})
        phone_and_tablet_serializer = Phone_TabletSerializer(phone_and_tablet, many=True, context={'request': request})
        sporting_goods_serializer = Sport_GoodingSerializer(sporting_goods, many=True, context={'request': request})
        tv_and_audio_serializer = Tv_AudioSerializer(tv_and_audio, many=True, context={'request': request})

        data = (
            appliances_serializer.data +
            baby_products_serializer.data +
            computersandaccessories_serializer.data +
            fashion_serializer.data +
            gaming_serializer.data +
            groceries_serializer.data +
            health_and_beauty_serializer.data +
            home_and_office_serializer.data +
            other_products_serializer.data +
            phone_and_tablet_serializer.data +
            sporting_goods_serializer.data +
            tv_and_audio_serializer.data
        )

        return Response(data, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.apps import apps
from django.conf import settings
from locations.models import County, SubCounty, Locality


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def creating_product_data_view(request):
    result = {"products": [], "services": []}

    def create_location_hierarchy():
        all_counties = County.objects.all()
        location_hierarchy = []

        for county in all_counties:
            county_data = {"county": county.name, "subcounties": []}

            for subcounty in SubCounty.objects.filter(county=county):
                subcounty_data = {"subcounty": subcounty.name, "regions": []}

                for region in Locality.objects.filter(subcounty=subcounty):
                    subcounty_data["regions"].append(region.name)

                county_data["subcounties"].append(subcounty_data)

            location_hierarchy.append(county_data)

        return location_hierarchy


    location_data = create_location_hierarchy()

    # Loop over product apps
    for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
        app_data = {"app_name": app_name, "models": []}
        process_app_data(app_data, app_name, BaseProduct, result['products'], location_data)

    # Loop over service apps
    for app_name in settings.ECOMMERCE_SERVICE_APPS:
        app_data = {"app_name": app_name, "models": []}
        process_app_data(app_data, app_name, BaseService, result['services'], location_data)

    return Response(result)
def process_app_data(app_data, app_name, base_class, result_list, location_data):
    excluded_fields = ["owner", "currency", "sponsored", "id", "updated", "created", "featured", "new", "most_sold", "out_of_stock", "product_serial", "slug", "service_serial","created_at","updated_at"]

    try:
        app_config = apps.get_app_config(app_name)
        for model in app_config.get_models():
            if issubclass(model, base_class):
                fields = [field.name for field in model._meta.fields if field.name not in excluded_fields]
                related_objects = {}

                for field in model._meta.get_fields():
                    if field.is_relation and field.related_model:
                        related_model = field.related_model
                        if field.name == "region":
                            related_objects[field.name] = location_data
                        elif field.name not in excluded_fields and field.name not in ['category', 'subcategory', 'type']:
                            related_objects[field.name] = list(related_model.objects.values_list('name', flat=True))

                if "category" in fields:
                    category_model = model.category.field.related_model
                    categories = category_model.objects.order_by('name').values_list('name', flat=True).distinct()

                    related_objects['category'] = []

                    for category in categories:
                        category_data = {'category': category, 'subcategories': []}

                        subcategories_model = model.subcategory.field.related_model
                        subcategories = subcategories_model.objects.filter(category__name=category).order_by('name').values_list('name', flat=True).distinct()

                        for subcategory in subcategories:
                            subcategory_data = {'subcategory': subcategory, 'types': []}

                            types_model = model.type.field.related_model
                            types = types_model.objects.filter(subcategory__name=subcategory).order_by('name').values_list('name', flat=True).distinct()

                            subcategory_data['types'] = list(types)
                            category_data['subcategories'].append(subcategory_data)

                        related_objects['category'].append(category_data)

                app_data['models'].append({'model_name': model.__name__, 'fields': fields, 'related_objects': related_objects})
    except LookupError:
        pass

    if app_data['models']:
        result_list.append(app_data)


 #######################
#  experiment 
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def experiment_data_view(request):
    result = {"products": [], "services": []}

    # Loop over product apps
    for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
        app_data = {"app_name": app_name, "categories": []}
        try:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseProduct):
                    # Process categories and subcategories
                    categories = model.objects.order_by('category__name').values_list('category__name', flat=True).distinct()
                    for category in categories:
                        category_data = {'category': category, 'subcategories': []}
                        subcategories = model.objects.filter(category__name=category).order_by('subcategory__name').values_list('subcategory__name', flat=True).distinct()
                        for subcategory in subcategories:
                            subcategory_data = {'subcategory': subcategory, 'types': []}
                            types = model.objects.filter(subcategory__name=subcategory).order_by('type__name').values_list('type__name', flat=True).distinct()
                            for type_name in types:
                                subcategory_data['types'].append(type_name)
                            category_data['subcategories'].append(subcategory_data)
                        app_data['categories'].append(category_data)
        except LookupError:
            pass

        if app_data['categories']:
            result['products'].append(app_data)

    return Response(result)



 #######################
#  experiment two
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def view_as_experiment_two(request):
    result = {'services': []}
    for app_name in settings.ECOMMERCE_SERVICE_APPS:
        app_data = {"app_name": app_name, "categories": []}
        try:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseService):
                    # Process categories and subcategories
                    categories = model.objects.order_by('category__name').values_list('category__name', flat=True).distinct()
                    for category in categories:
                        category_data = {'category': category, 'subcategories': []}
                        subcategories = model.objects.filter(category__name=category).order_by('subcategory__name').values_list('subcategory__name', flat=True).distinct()
                        for subcategory in subcategories:
                            subcategory_data = {'subcategory': subcategory, 'types': []}
                            types = model.objects.filter(subcategory__name=subcategory).order_by('type__name').values_list('type__name', flat=True).distinct()
                            for type_name in types:
                                subcategory_data['types'].append({'type': type_name})
                            category_data['subcategories'].append(subcategory_data)
                        app_data['categories'].append(category_data)
        except LookupError:
            pass

        if app_data['categories']:
            result['services'].append(app_data)

    return Response(result)

# import logging
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from django.apps import apps
# from django.conf import settings
# from products.models import BaseProduct
# from services.models import BaseService
# from profiles.models import Profile
# from business.models import Business
# from rest_framework.permissions import IsAuthenticated

# logger = logging.getLogger(__name__)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def creating_product_services_view(request):
#     # Retrieve the business owner
#     user = request.user
#     profile = Profile.objects.get(user=user.id)

#     business = Business.objects.get(owner=user.id)

#     data = request.data
#     selectedAppName = data.get('selectedAppName')
#     selectedType = data.get('selectedType')

#     logger.debug(f"selectedType: {selectedType}")
#     logger.debug(f"selectedAppName: {selectedAppName}")

#     if selectedType == "products":
#         app_list = settings.ECOMMERCE_PRODUCTS_APPS
#     elif selectedType == "services":
#         app_list = settings.ECOMMERCE_SERVICE_APPS
#     else:
#         return Response({"error": "Invalid selectedType value"})

#     if selectedAppName not in app_list:
#         return Response({"error": "Selected app not found"})

#     try:
#         app_config = apps.get_app_config(selectedAppName)
#         selectedModel = None

#         for model in app_config.get_models():
#             if issubclass(model, BaseProduct) or issubclass(model, BaseService):
#                 selectedModel = model
#                 break

#         if not selectedModel:
#             return Response({"error": "Selected model not found"})

#         # Rest of the code...

#     except LookupError:
#         return Response({"error": "Error retrieving models"})

#     return Response(models)




class AllProductsBusinessView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        user = request.user.id
        profile = Profile.objects.get(user=user)
        businesses = Business.objects.filter(owner=profile.id)
        products = []

        for business in businesses:
            appliances = ApplianceFilter(data={'search': search}, queryset=Appliance.objects.filter(owner=business)).qs
            baby_products = BabyProductFilter(data={'search': search}, queryset=BabyProduct.objects.filter(owner=business)).qs
            computersandaccessories = ComputingFilter(data={'search': search}, queryset=Computing.objects.filter(owner=business)).qs
            fashion = FashionFilter(data={'search': search}, queryset=Fashion.objects.filter(owner=business)).qs
            gaming = GamingFilter(data={'search': search}, queryset=Gaming.objects.filter(owner=business)).qs
            groceries = GroceryFilter(data={'search': search}, queryset=Grocery.objects.filter(owner=business)).qs
            health_and_beauty = Health_BeautyFilter(data={'search': search}, queryset=Health_Beauty.objects.filter(owner=business)).qs
            home_and_office = Home_OfficeFilter(data={'search': search}, queryset=Home_Office.objects.filter(owner=business)).qs
            other_products = Other_ProductFilter(data={'search': search}, queryset=Other_Product.objects.filter(owner=business)).qs
            phone_and_tablet = Phone_TabletFilter(data={'search': search}, queryset=Phone_Tablet.objects.filter(owner=business)).qs
            sporting_goods = Sport_GoodingFilter(data={'search': search}, queryset=Sport_Gooding.objects.filter(owner=business)).qs
            tv_and_audio = Tv_AudioFilter(data={'search': search}, queryset=Tv_Audio.objects.filter(owner=business)).qs

            appliances_serializer = ApplianceSerializer(appliances, many=True, context={'request': request})
            baby_products_serializer = BabyProductSerializer(baby_products, many=True, context={'request': request})
            computersandaccessories_serializer = ComputingSerializer(computersandaccessories, many=True, context={'request': request})
            fashion_serializer = FashionSerializer(fashion, many=True, context={'request': request})
            gaming_serializer = GamingSerializer(gaming, many=True, context={'request': request})
            groceries_serializer = GrocerySerializer(groceries, many=True, context={'request': request})
            health_and_beauty_serializer = Health_BeautySerializer(health_and_beauty, many=True, context={'request': request})
            home_and_office_serializer = Home_OfficeSerializer(home_and_office, many=True, context={'request': request})
            other_products_serializer = Other_ProductSerializer(other_products, many=True, context={'request': request})
            phone_and_tablet_serializer = Phone_TabletSerializer(phone_and_tablet, many=True, context={'request': request})
            sporting_goods_serializer = Sport_GoodingSerializer(sporting_goods, many=True, context={'request': request})
            tv_and_audio_serializer = Tv_AudioSerializer(tv_and_audio, many=True, context={'request': request})

            products += (
                appliances_serializer.data +
                baby_products_serializer.data +
                computersandaccessories_serializer.data +
                fashion_serializer.data +
                gaming_serializer.data +
                groceries_serializer.data +
                health_and_beauty_serializer.data +
                home_and_office_serializer.data +
                other_products_serializer.data +
                phone_and_tablet_serializer.data +
                sporting_goods_serializer.data +
                tv_and_audio_serializer.data
            )

        return Response(products, status=status.HTTP_200_OK)






@api_view(['GET'])

@permission_classes([IsAuthenticated])
def all_product_view_merchant(request, product_serial, format=None):
    appliances = Appliance.objects.filter(product_serial=product_serial)
    baby_products = BabyProduct.objects.filter(product_serial=product_serial)
    computersandaccessories = Computing.objects.filter(product_serial=product_serial)
    fashion = Fashion.objects.filter(product_serial=product_serial)
    gaming = Gaming.objects.filter(product_serial=product_serial)
    groceries = Grocery.objects.filter(product_serial=product_serial)
    health_and_beauty = Health_Beauty.objects.filter(product_serial=product_serial)
    home_and_office = Home_Office.objects.filter(product_serial=product_serial)
    other_products = Other_Product.objects.filter(product_serial=product_serial)
    phone_and_tablet = Phone_Tablet.objects.filter(product_serial=product_serial)
    sporting_goods = Sport_Gooding.objects.filter(product_serial=product_serial)
    tv_and_audio = Tv_Audio.objects.filter(product_serial=product_serial)

    appliances_serializer = ApplianceSerializer(appliances, many=True, context={'request': request})
    baby_products_serializer = BabyProductSerializer(baby_products, many=True, context={'request': request})
    computersandaccessories_serializer = ComputingSerializer(computersandaccessories, many=True, context={'request': request})
    fashion_serializer = FashionSerializer(fashion, many=True, context={'request': request})
    gaming_serializer = GamingSerializer(gaming, many=True, context={'request': request})
    groceries_serializer = GrocerySerializer(groceries, many=True, context={'request': request})
    health_and_beauty_serializer = Health_BeautySerializer(health_and_beauty, many=True, context={'request': request})
    home_and_office_serializer = Home_OfficeSerializer(home_and_office, many=True, context={'request': request})
    other_products_serializer = Other_ProductSerializer(other_products, many=True, context={'request': request})
    phone_and_tablet_serializer = Phone_TabletSerializer(phone_and_tablet, many=True, context={'request': request})
    sporting_goods_serializer = Sport_GoodingSerializer(sporting_goods, many=True, context={'request': request})
    tv_and_audio_serializer = Tv_AudioSerializer(tv_and_audio, many=True, context={'request': request})

    data = (
        appliances_serializer.data +
        baby_products_serializer.data +
        computersandaccessories_serializer.data +
        fashion_serializer.data +
        gaming_serializer.data +
        groceries_serializer.data +
        health_and_beauty_serializer.data +
        home_and_office_serializer.data +
        other_products_serializer.data +
        phone_and_tablet_serializer.data +
        sporting_goods_serializer.data +
        tv_and_audio_serializer.data
    )

    return Response(data, status=status.HTTP_200_OK)


class AllProductsAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        
        products = []

        
        appliances = ApplianceFilter(data={'search': search}, queryset=Appliance.objects.all()).qs
        baby_products = BabyProductFilter(data={'search': search}, queryset=BabyProduct.objects.all()).qs
        computersandaccessories = ComputingFilter(data={'search': search}, queryset=Computing.objects.all()).qs
        fashion = FashionFilter(data={'search': search}, queryset=Fashion.objects.all()).qs
        gaming = GamingFilter(data={'search': search}, queryset=Gaming.objects.all()).qs
        groceries = GroceryFilter(data={'search': search}, queryset=Grocery.objects.all()).qs
        health_and_beauty = Health_BeautyFilter(data={'search': search}, queryset=Health_Beauty.objects.all()).qs
        home_and_office = Home_OfficeFilter(data={'search': search}, queryset=Home_Office.objects.all()).qs
        other_products = Other_ProductFilter(data={'search': search}, queryset=Other_Product.objects.all()).qs
        phone_and_tablet = Phone_TabletFilter(data={'search': search}, queryset=Phone_Tablet.objects.all()).qs
        sporting_goods = Sport_GoodingFilter(data={'search': search}, queryset=Sport_Gooding.objects.all()).qs
        tv_and_audio = Tv_AudioFilter(data={'search': search}, queryset=Tv_Audio.objects.all()).qs

        appliances_serializer = ApplianceSerializer(appliances, many=True, context={'request': request})
        baby_products_serializer = BabyProductSerializer(baby_products, many=True, context={'request': request})
        computersandaccessories_serializer = ComputingSerializer(computersandaccessories, many=True, context={'request': request})
        fashion_serializer = FashionSerializer(fashion, many=True, context={'request': request})
        gaming_serializer = GamingSerializer(gaming, many=True, context={'request': request})
        groceries_serializer = GrocerySerializer(groceries, many=True, context={'request': request})
        health_and_beauty_serializer = Health_BeautySerializer(health_and_beauty, many=True, context={'request': request})
        home_and_office_serializer = Home_OfficeSerializer(home_and_office, many=True, context={'request': request})
        other_products_serializer = Other_ProductSerializer(other_products, many=True, context={'request': request})
        phone_and_tablet_serializer = Phone_TabletSerializer(phone_and_tablet, many=True, context={'request': request})
        sporting_goods_serializer = Sport_GoodingSerializer(sporting_goods, many=True, context={'request': request})
        tv_and_audio_serializer = Tv_AudioSerializer(tv_and_audio, many=True, context={'request': request})

        products += (
            appliances_serializer.data +
            baby_products_serializer.data +
            computersandaccessories_serializer.data +
            fashion_serializer.data +
            gaming_serializer.data +
            groceries_serializer.data +
            health_and_beauty_serializer.data +
            home_and_office_serializer.data +
            other_products_serializer.data +
            phone_and_tablet_serializer.data +
            sporting_goods_serializer.data +
            tv_and_audio_serializer.data
        )

        return Response(products, status=status.HTTP_200_OK)