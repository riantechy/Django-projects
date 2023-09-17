from django.urls import path
from .views import *

urlpatterns = [
    path('products/healthandbeauty/', Health_BeautyList.as_view(), name='get_healthandbeauty'),    
    path('healthandbeauty/create/', CreateHealth_BeautyAPIView.as_view(), name='create_healthandbeauty'),
    path('products/healthandbeauty/<str:category>/', Health_BeautyByCategory.as_view(), name='healthandbeauty_by_category'),
    path('products/healthandbeauty/<str:category>/<str:subcategory>/', Health_BeautyBySubcategory.as_view(), name='healthandbeauty_by_subcategory'),
    path('products/healthandbeauty/<str:category>/<str:subcategory>/<str:type>/',Health_BeautyByType.as_view(), name='healthandbeauty_by_type'),
    path('products/healthandbeauty/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Health_BeautyDetailView.as_view(), name='Health_Beauty_detail'),
]   
 