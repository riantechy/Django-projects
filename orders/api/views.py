from rest_framework import generics, permissions
from orders.models import Product_Order, Service_Order
from .serializers import ProductOrderSerializer, ServiceOrderSerializer
from django.shortcuts import get_object_or_404
from django.apps import apps
from django.core.exceptions import AppRegistryNotReady
from products.models import BaseProduct
from services.models import BaseService
from django.core.exceptions import FieldDoesNotExist
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status ,generics
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Product_Order
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Account
from  business.models import Business
from rest_framework.generics import ListCreateAPIView
from profiles.models import Profile


class AdminProductOrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductOrderSerializer

    def get_queryset(self):        
        queryset = Product_Order.objects.all()
        return queryset
    
class AdminServiceOrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceOrderSerializer

    def get_queryset(self):        
        queryset = Service_Order.objects.all()
        return queryset

class MerchantServiceOrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceOrderSerializer

    def get_queryset(self):
        user = self.request.user.id
        account = Account.objects.get(id=user)
        profile = Profile.objects.get(user=account)

        try:
            business = Business.objects.get(owner=profile)
            queryset = Service_Order.objects.filter(business=business)
        except Business.DoesNotExist:
            queryset = Service_Order.objects.none()  # Return an empty queryset

        return queryset


class CustomerServiceOrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceOrderSerializer

    def get_queryset(self):
        user = self.request.user.id
        account = Account.objects.get(id=user)
        queryset = Service_Order.objects.filter(customer=account)
        return queryset
        

class MerchantProductOrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductOrderSerializer

    def get_queryset(self):
        user = self.request.user.id
        account = Account.objects.get(id=user)
        profile = Profile.objects.get(user=account)

        try:
            business = Business.objects.get(owner=profile)
            queryset = Product_Order.objects.filter(business=business)
        except Business.DoesNotExist:
            queryset = Product_Order.objects.none()  # Return an empty queryset

        return queryset

        return queryset

class ProductOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductOrderSerializer

    def get_queryset(self):
        user = self.request.user.id
        account = Account.objects.get(id=user)
        queryset = Product_Order.objects.filter(customer=account)
        return queryset

    def create(self, request, *args, **kwargs):
        user = self.request.user.id
        account = Account.objects.get(id=user)
        try:
            product_list = request.data  # Assuming the request data is a list of product objects
            profile=Profile.objects.filter(user=account,verified=True)
            if not profile:
                return Response({'error':'Complete Your Profile'},status=424)

            

            # Fetch all the app names present in the product list
            app_names = set([product.get('app_name') for product in product_list])

            # Fetch all the models that inherit from BaseProduct in the specified app_names
            app_models = []
            for app_name in app_names:
                try:
                    models = apps.get_app_config(app_name).get_models()
                    app_models.extend([
                        model
                        for model in models
                        if issubclass(model, BaseProduct)
                    ])
                except apps.exceptions.AppRegistryNotReady:
                    return Response({'error': 'Invalid app name or models not found'}, status=status.HTTP_400_BAD_REQUEST)

            product_orders = []  # List to hold the product order data

            # Get the customer account
            customer = Account.objects.get(id=request.user.id)

            # Process each product individually
            for product_data in product_list:
                product_serial = product_data.get('product_serial', '')
                app_name = product_data.get('app_name', '')
                product_title = product_data.get('title', '')
                business = product_data.get('business')

                # Find the model class for the product's app_name
                model_class = next((model for model in app_models if model._meta.app_label == app_name), None)
                if not model_class:
                    return Response({'error': f'Invalid app name or models not found for {app_name}'}, status=status.HTTP_400_BAD_REQUEST)

                # Check if product_serial already exists in the specific model
                product_exists = model_class.objects.filter(product_serial=product_serial).exists()
                if not product_exists:
                    return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)

                # Get the business ID from the existing product
                product = model_class.objects.get(product_serial=product_serial)
                business_owner = product.owner.id            
                try:
                    business = Business.objects.get(id=business_owner)
                except ObjectDoesNotExist:
                    return Response({'error': 'Business does not exist'}, status=status.HTTP_400_BAD_REQUEST)

                # Check if product_serial already exists in Product_Order model
                if Product_Order.objects.filter(product_serial=product_serial, customer=customer).exists():
                    return Response({'error': f'{product_title} already exists in your orders'}, status=status.HTTP_400_BAD_REQUEST)

                product_order_data = Product_Order(
                    customer=customer,
                    product_serial=product_serial,
                    product_type=ContentType.objects.get_for_model(model_class),
                    product_id=product.id,
                    business=business,
                )

                product_orders.append(product_order_data)

            # Bulk create the product orders
            Product_Order.objects.bulk_create(product_orders)
            return Response({'message': 'Orders Placed Successfully!!'}, status=status.HTTP_201_CREATED)
        
        except ContentType.DoesNotExist:
            return Response({'error': 'Invalid app name or models not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([AllowAny])

def service_order_view(request):
    if request.method == 'GET':
        queryset = Service_Order.objects.all()
        serializer = ServiceOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        # Retrieve the user ID
        service_list = request.data  # Assuming the request data is a list of service objects

        for service_data in service_list:
            service_serial = service_data.get('service_serial', '')
            app_name = service_data.get('app_name', '')
            customer = request.user.id
            business = service_data.get('business')

            try:
                app_models = apps.get_app_config(app_name).get_models()
                model_names = [
                    model._meta.model_name
                    for model in app_models
                    if issubclass(model, BaseService)
                ]
                content_type = ContentType.objects.get(app_label=app_name, model__in=model_names)
                model_class = content_type.model_class()  # Get the model class dynamically

                # Check if service_serial already exists in the specific model
                service_exists = model_class.objects.filter(service_serial=service_serial).exists()
                if not service_exists:
                    return Response({'error': 'Service does not exist'}, status=400)

                # Get the service ID from the existing service
                existing_service = model_class.objects.get(service_serial=service_serial)
                service_id = existing_service.id

                # Check if service_serial already exists in Service_Order model
                if Service_Order.objects.filter(service_serial=service_serial).exists():
                    return Response({'error': 'Service already exists in orders'}, status=400)

                service_order_data = {
                    'customer': customer,
                    'service_serial': service_serial,
                    'service_type': content_type.pk,
                    'service_id': service_id,
                    'business': business,
                }

                serializer = ServiceOrderSerializer(data=service_order_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)

            except (AppRegistryNotReady, ContentType.DoesNotExist):
                return Response({'error': 'Invalid app name or models not found'}, status=400)

        return Response({'message': 'Services created successfully'}, status=201)


class ProductOrderDetailView(generics.RetrieveAPIView):
    queryset = Product_Order.objects.all()
    serializer_class = ProductOrderSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        unique_code = self.kwargs['search']
        order = get_object_or_404(Product_Order, order_number=unique_code)
        return order

class ServiceOrderDetailView(generics.RetrieveAPIView):
    queryset = Service_Order.objects.all()
    serializer_class = ServiceOrderSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        unique_code = self.kwargs['search']
        order = get_object_or_404(Service_Order, order_number=unique_code)
        return order
