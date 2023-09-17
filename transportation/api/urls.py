from django.urls import path
from .views import *

urlpatterns = [
    path('services/transportation/', TransportList.as_view(), name='get_transportation_services'),    
    path('transportation/create/',   CreateTransportAPIView.as_view(), name='create_transportation'),
    path('services/transportation/<str:category>/', TransportByCategory.as_view(), name='transportation_by_category_services'),
    path('services/transportation/<str:category>/<str:subcategory>/', TransportBySubcategory.as_view(), name='transportation_by_subcategory_services'),
    path('services/transportation/<str:category>/<str:subcategory>/<str:type>/',TransportByType.as_view(), name='transportation_by_type_services'),
    path('services/transportation/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',TransportDetailView.as_view(), name='Transport_service_detail'),
]   
 