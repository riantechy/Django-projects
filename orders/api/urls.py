from django.urls import path
from .views import MerchantServiceOrderListAPIView,CustomerServiceOrderListAPIView,AdminServiceOrderListAPIView,MerchantProductOrderListAPIView,AdminProductOrderListAPIView,ProductOrderListAPIView, ProductOrderDetailView, service_order_view, ServiceOrderDetailView

urlpatterns = [
    path('product_orders/', ProductOrderListAPIView.as_view(), name='customer-product_order-list'),
    path('merchant/product_orders/', MerchantProductOrderListAPIView.as_view(), name='merchant-product_order-list'),
    path('admin/product_orders/', AdminProductOrderListAPIView.as_view(), name='admin-product_order-list'),
    path('admin/service_orders/', AdminServiceOrderListAPIView.as_view(), name='admin-service-order-list'),
    path('merchant/service_orders/', MerchantServiceOrderListAPIView.as_view(), name='merchant-service-admin-list'),
    path('service_orders/',CustomerServiceOrderListAPIView.as_view(), name='service_order-list'),
    path('product_orders/<str:search>/', ProductOrderDetailView.as_view(), name='product_order-detail'),
    
    path('service_orders/<str:search>/', ServiceOrderDetailView.as_view(), name='service_order-detail'),
]
