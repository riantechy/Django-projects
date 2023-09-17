from django.urls import path
from .views import *

urlpatterns = [
    path('products/tvandaudio/', Tv_AudioList.as_view(), name='get_tvandaudio'),    
    path('tvandaudio/create/', CreateTv_AudioAPIView.as_view(), name='create_tvandaudio'),
    path('products/tvandaudio/<str:category>/', Tv_AudioByCategory.as_view(), name='tvandaudio_by_category'),
    path('products/tvandaudio/<str:category>/<str:subcategory>/', Tv_AudioBySubcategory.as_view(), name='tvandaudio_by_subcategory'),
    path('products/tvandaudio/<str:category>/<str:subcategory>/<str:type>/',Tv_AudioByType.as_view(), name='tvandaudio_by_type'),
    path('products/tvandaudio/<str:category>/<str:subcategory>/<str:type>/<str:product_serial>/',Tv_AudioDetailView.as_view(), name='Tv_Audio_detail'),
]   
 