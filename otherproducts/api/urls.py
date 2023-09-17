from django.urls import path
from .views import *

urlpatterns = [
    path('products/otherproducts/', Other_ProductList.as_view(), name='get_otherproducts'),    
    path('otherproducts/create/', CreateOther_ProductAPIView.as_view(), name='create_otherproducts'),
    path('products/otherproducts/<str:category>/', Other_ProductByCategory.as_view(), name='otherproducts_by_category'),
    path('products/otherproducts/<str:category>/<str:subcategory>/', Other_ProductBySubcategory.as_view(), name='otherproducts_by_subcategory'),
    path('products/otherproducts/<str:category>/<str:subcategory>/<str:type>/',Other_ProductByType.as_view(), name='otherproducts_by_type'),
    path('products/otherproducts/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Other_ProductDetailView.as_view(), name='Other_Product_detail'),
]   
 