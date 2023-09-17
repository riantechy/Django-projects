from django.urls import path
from .views import *

urlpatterns = [
    path('products/gaming/', GamingList.as_view(), name='get_gaming'),    
    path('gaming/create/', CreateGamingAPIView.as_view(), name='create_gaming'),
    path('products/gaming/<str:category>/', GamingByCategory.as_view(), name='gaming_by_category'),
    path('products/gaming/<str:category>/<str:subcategory>/', GamingBySubcategory.as_view(), name='gaming_by_subcategory'),
    path('products/gaming/<str:category>/<str:subcategory>/<str:type>/',GamingByType.as_view(), name='gaming_by_type'),
    path('products/gaming/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',GamingDetailView.as_view(), name='Gaming_detail'),
]   
 