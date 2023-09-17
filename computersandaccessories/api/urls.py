from django.urls import path
from .views import *

urlpatterns = [
    path('products/computersandaccessories/', ComputingList.as_view(), name='get_computers&accessories'),    
    path('computersandaccessories/create/', CreateComputingAPIView.as_view(), name='create_computersandaccessories'),
    path('products/computersandaccessories/<str:category>/', ComputingByCategory.as_view(), name='computers&accessories_by_category'),
    path('products/computersandaccessories/<str:category>/<str:subcategory>/', ComputingBySubcategory.as_view(), name='computers&accessories_by_subcategory'),
    path('products/computersandaccessories/<str:category>/<str:subcategory>/<str:type>/',ComputingByType.as_view(), name='computers&accessories_by_type'),
    path('products/computersandaccessories/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',ComputingDetailView.as_view(), name='Computing_detail'),
]   
 