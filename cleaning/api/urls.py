from django.urls import path
from .views import *

urlpatterns = [
    path('services/cleaning/', CleaningList.as_view(), name='get_cleaning_services'),    
    path('cleaning/create/',   CreateCleaningAPIView.as_view(), name='create_cleaning'),
    path('services/cleaning/<str:category>/', CleaningByCategory.as_view(), name='cleaning_by_category_services'),
    path('services/cleaning/<str:category>/<str:subcategory>/', CleaningBySubcategory.as_view(), name='cleaning_by_subcategory_services'),
    path('services/cleaning/<str:category>/<str:subcategory>/<str:type>/',CleaningByType.as_view(), name='cleaning_by_type_services'),
    path('services/cleaning/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',CleaningDetailView.as_view(), name='Cleaning_service_detail'),
]   
 