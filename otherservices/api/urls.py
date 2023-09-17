from django.urls import path
from .views import *

urlpatterns = [
    path('services/otherservices/', Other_ServiceList.as_view(), name='get_otherservices_services'),    
    path('otherservices/create/',   CreateOther_ServiceAPIView.as_view(), name='create_otherservices'),
    path('services/otherservices/<str:category>/', Other_ServiceByCategory.as_view(), name='otherservices_by_category_services'),
    path('services/otherservices/<str:category>/<str:subcategory>/', Other_ServiceBySubcategory.as_view(), name='otherservices_by_subcategory_services'),
    path('services/otherservices/<str:category>/<str:subcategory>/<str:type>/',Other_ServiceByType.as_view(), name='otherservices_by_type_services'),
    path('services/otherservices/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',Other_ServiceDetailView.as_view(), name='Other_Service_service_detail'),
]   
 