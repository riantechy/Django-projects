from django.urls import path
from .views import  ApplianceList,AppliancesByCategory,AppliancesBySubcategory,AppliancesByType,ApplianceDetailView,CreateApplianceAPIView ,ApplianceEdit


urlpatterns = [
    path('products/appliances/', ApplianceList.as_view(), name='get_appliances'),    
    path('appliances/edit/<str:product_serial>/', ApplianceEdit.as_view(), name='edit_appliances'),
    path('appliances/create/', CreateApplianceAPIView.as_view(), name='create_appliances'),
    path('products/appliances/<str:category>/', AppliancesByCategory.as_view(), name='appliances_by_category'),
    path('products/appliances/<str:category>/<str:subcategory>/', AppliancesBySubcategory.as_view(), name='appliances_by_subcategory'),
    path('products/appliances/<str:category>/<str:subcategory>/<str:type>/',AppliancesByType.as_view(), name='appliances_by_type'),
    path('products/appliances/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',ApplianceDetailView.as_view(), name='appliance_detail'),
]   
 