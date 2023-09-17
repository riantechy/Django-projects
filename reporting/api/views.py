from django.conf import settings
from django.apps import apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Product_Order, Service_Order
from business.models import Business
from  profiles.models import Profile
from accounts.models import Account
from products.models import BaseProduct
from services.models import BaseService
from accounts.models import  Customer,Merchant

class CustomerReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.id
        product_count = Product_Order.objects.filter(customer=user).count()
        service_count = Service_Order.objects.filter(customer=user).count()
        data = {
            'product_total_orders': product_count,
            'service_total_orders': service_count
        }
        return Response(data)




class MerchantReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user.id
        account = Account.objects.get(id=user)
        profile = Profile.objects.get(user=account)
        business_instance = Business.objects.get(owner=profile)
        business_count = Business.objects.filter(owner=profile).count()
        customer_product_count = Product_Order.objects.filter(business=business_instance).values('customer').distinct().count()
        customer_service_count = Service_Order.objects.filter(business=business_instance).values('customer').distinct().count()
        product_order_count =Product_Order.objects.filter(business=business_instance).count()
        service_order_count =Service_Order.objects.filter(business=business_instance).count()
        product_count = self.get_product_count(business_instance)
        service_count = self.get_service_count(business_instance)

        data = {
            'product_total_orders': product_order_count,
            'service_total_orders': service_order_count,
            'business_count': business_count,
            'product_count': product_count,
            'service_count':service_count,
            'customer_count': customer_product_count  + customer_service_count
        }
        return Response(data)

    def get_product_count(self, business_instance):
        product_count = 0
        for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseProduct):
                    app_product_count = model.objects.filter(owner=business_instance).count()
                    product_count += app_product_count
        return product_count

    def get_service_count(self, business_instance):
        service_count = 0
        for app_name in settings.ECOMMERCE_SERVICE_APPS:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseService):
                    app_service_count = model.objects.filter(owner=business_instance).count()
                    service_count += app_service_count
        return service_count




from django.core.cache import cache

class AdminReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        business_count = cache.get('business_count')
        merchant_count = cache.get('merchant_count')
        customers_count = cache.get('customers_count')
        customer_product_count = cache.get('customer_product_count')
        customer_service_count = cache.get('customer_service_count')
        product_count = cache.get('product_count')
        product_order_count = cache.get('product_order_count')
        service_order_count = cache.get('service_order_count')
        service_count = cache.get('service_count')

        if business_count is None:
            business_count = Business.objects.all().count()
            cache.set('business_count', business_count, 300)  # Cache for 5 minutes

        if merchant_count is None:
            merchant_count = Merchant.objects.all().count()
            cache.set('merchant_count', merchant_count, 300)  # Cache for 5 minutes

        if customers_count is None:
            customers_count = Customer.objects.all().count()
            cache.set('customers_count', customers_count, 300)  # Cache for 5 minutes

        if customer_product_count is None:
            customer_product_count = Product_Order.objects.all().values('customer').distinct().count()
            cache.set('customer_product_count', customer_product_count, 300)  # Cache for 5 minutes

        if customer_service_count is None:
            customer_service_count = Service_Order.objects.all().values('customer').distinct().count()
            cache.set('customer_service_count', customer_service_count, 300)  # Cache for 5 minutes

        if product_count is None:
            product_count = self.get_product_count()
            cache.set('product_count', product_count, 300)  # Cache for 5 minutes
        if product_order_count is None:
            product_order_count = Product_Order.objects.all().count()
            cache.set('product_order_count', product_order_count, 300) 
        if service_order_count is None:
            service_order_count = Service_Order.objects.all().count()
            cache.set('service_order_count', service_order_count, 300) 

        if service_count is None:
            service_count = self.get_service_count()
            cache.set('service_count', service_count, 300)  # Cache for 5 minutes

        data = {
            'customer_count': customers_count,
            'merchant_count': merchant_count,
            'business_count': business_count,
            'product_count': product_count,
            'service_count': service_count,
            'product_total_orders': product_order_count,
            'service_total_orders': service_order_count,
            'customer_with_orders': customer_product_count + customer_service_count
        }
        return Response(data)

    def get_product_count(self):
        product_count = 0
        for app_name in settings.ECOMMERCE_PRODUCTS_APPS:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseProduct):
                    app_product_count = model.objects.all().count()
                    product_count += app_product_count
        return product_count

    def get_service_count(self):
        service_count = 0
        for app_name in settings.ECOMMERCE_SERVICE_APPS:
            app_config = apps.get_app_config(app_name)
            for model in app_config.get_models():
                if issubclass(model, BaseService):
                    app_service_count = model.objects.all().count()
                    service_count += app_service_count
        return service_count
