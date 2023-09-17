from django.urls import path
from .views import *

urlpatterns = [
    path('products/phoneandtablet/', Phone_TabletList.as_view(), name='get_phoneandtablet'),    
    path('phoneandtablet/create/', CreatePhone_TabletAPIView.as_view(), name='create_phoneandtablet'),
    path('products/phoneandtablet/<str:category>/', Phone_TabletByCategory.as_view(), name='phoneandtablet_by_category'),
    path('products/phoneandtablet/<str:category>/<str:subcategory>/', Phone_TabletBySubcategory.as_view(), name='phoneandtablet_by_subcategory'),
    path('products/phoneandtablet/<str:category>/<str:subcategory>/<str:type>/',Phone_TabletByType.as_view(), name='phoneandtablet_by_type'),
    path('products/phoneandtablet/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Phone_TabletDetailView.as_view(), name='Phone_Tablet_detail'),
]   
 