from django.urls import path
from .views import *

urlpatterns = [
    path('products/sporting/', Sport_GoodingList.as_view(), name='get_sporting'),    
    path('sporting/create/', CreateSport_GoodingAPIView.as_view(), name='create_sporting'),
    path('products/sporting/<str:category>/', Sport_GoodingByCategory.as_view(), name='sporting_by_category'),
    path('products/sporting/<str:category>/<str:subcategory>/', Sport_GoodingBySubcategory.as_view(), name='sporting_by_subcategory'),
    path('products/sporting/<str:category>/<str:subcategory>/<str:type>/',Sport_GoodingByType.as_view(), name='sporting_by_type'),
    path('products/sporting/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Sport_GoodingDetailView.as_view(), name='Sport_Gooding_detail'),
]   
 