from django.urls import path
from .views import *

urlpatterns = [
    path('products/homeandoffice/', Home_OfficeList.as_view(), name='get_homeandoffice'),    
    path('homeandoffice/create/', CreateHome_OfficeAPIView.as_view(), name='create_homeandoffice'),
    path('products/homeandoffice/<str:category>/', Home_OfficeByCategory.as_view(), name='homeandoffice_by_category'),
    path('products/homeandoffice/<str:category>/<str:subcategory>/', Home_OfficeBySubcategory.as_view(), name='homeandoffice_by_subcategory'),
    path('products/homeandoffice/<str:category>/<str:subcategory>/<str:type>/',Home_OfficeByType.as_view(), name='homeandoffice_by_type'),
    path('products/homeandoffice/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Home_OfficeDetailView.as_view(), name='Home_Office_detail'),
]   
 