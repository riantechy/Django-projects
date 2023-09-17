from django.urls import path
from .views import *

urlpatterns = [
    path('services/cateringandevent/', Catering_EventList.as_view(), name='get_cateringandevent_services'),    
    path('cateringandevent/create/',   CreateCatering_EventAPIView.as_view(), name='create_cateringandevent'),
    path('services/cateringandevent/<str:category>/', Catering_EventByCategory.as_view(), name='cateringandevent_by_category_services'),
    path('services/cateringandevent/<str:category>/<str:subcategory>/', Catering_EventBySubcategory.as_view(), name='cateringandevent_by_subcategory_services'),
    path('services/cateringandevent/<str:category>/<str:subcategory>/<str:type>/',Catering_EventByType.as_view(), name='cateringandevent_by_type_services'),
    path('services/cateringandevent/<str:category>/<str:subcategory>/<str:type>/<str:service_serial>/',Catering_EventDetailView.as_view(), name='Catering_Event_service_detail'),
]   
 