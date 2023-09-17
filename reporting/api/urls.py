from django.urls import path
from .views import CustomerReportView,MerchantReportView,AdminReportView

urlpatterns = [
    path('customer-report/', CustomerReportView.as_view(), name='customer-report'),
    path('merchant-report/', MerchantReportView.as_view(), name='merchant-report'),
    path('admin-report/', AdminReportView.as_view(), name='admin-report'),
]
