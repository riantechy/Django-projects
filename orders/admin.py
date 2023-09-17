from django.contrib import admin
from .models import Product_Order, Service_Order, OrderStatus

class Product_OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', 'business_name', 'product_title', 'created')
    search_fields = ('business__name', 'product_type__model', 'product_id')

admin.site.register(Product_Order, Product_OrderAdmin)

class Service_OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', 'business_name', 'service_id', 'created')
    search_fields = ('business__name', 'service_type__model', 'service_id')

admin.site.register(Service_Order, Service_OrderAdmin)
