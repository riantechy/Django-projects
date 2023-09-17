from django.urls import path
from .views import *

urlpatterns = [
    path('products/groceries/', GroceryList.as_view(), name='get_groceries'),    
    path('groceries/create/', CreateGroceryAPIView.as_view(), name='create_groceries'),
    path('products/groceries/<str:category>/', GroceryByCategory.as_view(), name='groceries_by_category'),
    path('products/groceries/<str:category>/<str:subcategory>/', GroceryBySubcategory.as_view(), name='groceries_by_subcategory'),
    path('products/groceries/<str:category>/<str:subcategory>/<str:type>/',GroceryByType.as_view(), name='groceries_by_type'),
    path('products/groceries/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',GroceryDetailView.as_view(), name='Grocery_detail'),
]   
 