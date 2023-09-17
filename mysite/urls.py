"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    # responsinle for account and registration of business
    path('api/', include('accounts.api.urls')),
    path('api/', include('profiles.api.urls')),
    path('api/', include('business.api.urls')),
    # our shopping categories and shops api
    path('api/', include('appliances.api.urls')),
    path('api/', include('baby_items.api.urls')),
    path('api/', include('computersandaccessories.api.urls')),
    path('api/', include('groceries.api.urls')),
    path('api/', include('fashion.api.urls')),
    path('api/', include('gaming.api.urls')),
    path('api/', include('products.api.urls')),
    path('api/', include('healthandbeauty.api.urls')),
    path('api/', include('homeandoffice.api.urls')),
    path('api/', include('otherproducts.api.urls')),
    path('api/', include('phoneandtablet.api.urls')),
    path('api/', include('sporting.api.urls')),
    path('api/', include('tvandaudio.api.urls')),
    
# our services apis 
    path('api/', include('services.api.urls')),
    path('api/', include('beauty.api.urls')),
    path('api/', include('cateringandevent.api.urls')),
    path('api/', include('cleaning.api.urls')),
    path('api/', include('computerandit.api.urls')),
    path('api/', include('mechanic.api.urls')),
    path('api/', include('transportation.api.urls')),
# orders
    path('api/', include('orders.api.urls')),
    # reporting 
    path('api/', include('reporting.api.urls')),

    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


