from django.urls import path
from .views import *

urlpatterns = [
    path('services/mechanic/', MechanicList.as_view(), name='get_mechanic_services'),    
    path('mechanic/create/',   CreateMechanicAPIView.as_view(), name='create_mechanic'),
    path('services/mechanic/<str:category>/', MechanicByCategory.as_view(), name='mechanic_by_category_services'),
    path('services/mechanic/<str:category>/<str:subcategory>/', MechanicBySubcategory.as_view(), name='mechanic_by_subcategory_services'),
    path('services/mechanic/<str:category>/<str:subcategory>/<str:type>/',MechanicByType.as_view(), name='mechanic_by_type_services'),
    path('services/mechanic/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',MechanicDetailView.as_view(), name='Mechanic_service_detail'),
]   
 