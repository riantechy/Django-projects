from django.urls import URLPattern, path
from .import views


urlpatterns = [
    path('', views.stores, name='stores'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.PostDetailView.as_view(), name='product-details'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]