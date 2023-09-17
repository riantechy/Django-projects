from django.urls import path
from .views import *

urlpatterns = [
    path('services/beauty/', BeautyList.as_view(), name='get_beauty_services'),    
    path('beauty/create/',   CreateBeautyAPIView.as_view(), name='create_beauty'),
    path('services/beauty/<str:category>/', BeautyByCategory.as_view(), name='beauty_by_category_services'),
    path('services/beauty/<str:category>/<str:subcategory>/', BeautyBySubcategory.as_view(), name='beauty_by_subcategory_services'),
    path('services/beauty/<str:category>/<str:subcategory>/<str:type>/',BeautyByType.as_view(), name='beauty_by_type_services'),
    path('services/beauty/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',BeautyDetailView.as_view(), name='Beauty_service_detail'),
]   
 