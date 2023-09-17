from django.urls import path
from .views import app_list,sidebar_data_view ,all_product_view_merchant,AllProductsAdminView,AllProductsView,AllProductsBusinessView ,creating_product_data_view,experiment_data_view ,view_as_experiment_two

urlpatterns = [
    path('products/navbar/', app_list),
    path('sidebar/', sidebar_data_view),
    path('experiment/', experiment_data_view),
    path('experiment/two/', view_as_experiment_two),
    path('productsandservices/', creating_product_data_view),
    # path('productsandservices/create/', creating_product_services_view),
    path('products/', AllProductsView.as_view(), name='all-products'),
    path('products/detail/<str:product_serial>/', all_product_view_merchant, name='Merchant Products'),
    path('products/business/', AllProductsBusinessView.as_view(), name='all-products'),
    path('products/admin/', AllProductsAdminView.as_view(), name='admin-all-products'),


]
