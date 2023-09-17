from django.urls import path
from .views import *

urlpatterns = [
    path('products/baby_items/', BabyProductList.as_view(), name='get_baby_items'),    
    path('baby_items/create/', CreateBabyProductAPIView.as_view(), name='create_baby_items'),
    path('products/baby_items/<str:category>/', BabyProductsByCategory.as_view(), name='baby_items_by_category'),
    path('products/baby_items/<str:category>/<str:subcategory>/', BabyProductsBySubcategory.as_view(), name='baby_items_by_subcategory'),
    path('products/baby_items/<str:category>/<str:subcategory>/<str:type>/',BabyProductsByType.as_view(), name='baby_items_by_type'),
    path('products/baby_items/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',BabyProductDetailView.as_view(), name='BabyProduct_detail'),
]   
 