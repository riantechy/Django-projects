from django.urls import path
from .views import app_list,AllServicesView,AllServicesAdminView

urlpatterns = [
    path('services/navbar/', app_list),
    path('services/', AllServicesView.as_view(), name='all-services'),
    path('services/admin/', AllServicesAdminView.as_view(), name='admin-all-services'),


]
