from django.urls import path
from .views import *

urlpatterns = [
    path('services/computerandit/', Computer_ItList.as_view(), name='get_computerandit_services'),    
    path('computerandit/create/',   CreateComputer_ItAPIView.as_view(), name='create_computerandit'),
    path('services/computerandit/<str:category>/', Computer_ItByCategory.as_view(), name='computerandit_by_category_services'),
    path('services/computerandit/<str:category>/<str:subcategory>/', Computer_ItBySubcategory.as_view(), name='computerandit_by_subcategory_services'),
    path('services/computerandit/<str:category>/<str:subcategory>/<str:type>/',Computer_ItByType.as_view(), name='computerandit_by_type_services'),
    path('services/computerandit/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',Computer_ItDetailView.as_view(), name='Computer_It_service_detail'),
]   
 