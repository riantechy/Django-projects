from django.urls import path
from .views import *

urlpatterns = [
    path('products/fashion/', FashionList.as_view(), name='get_fashion'),    
    path('fashion/create/', CreateFashionAPIView.as_view(), name='create_fashion'),
    path('products/fashion/<str:category>/', FashionByCategory.as_view(), name='fashion_by_category'),
    path('products/fashion/<str:category>/<str:subcategory>/', FashionBySubcategory.as_view(), name='fashion_by_subcategory'),
    path('products/fashion/<str:category>/<str:subcategory>/<str:type>/',FashionByType.as_view(), name='fashion_by_type'),
    path('products/fashion/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',FashionDetailView.as_view(), name='Fashion_detail'),
]   
 