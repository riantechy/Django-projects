# appliances/filters.py
import django_filters
from django.db.models import Q
from appliances.models import *
from baby_items.models import *
from computersandaccessories.models import *
from fashion.models import *
from gaming.models import *
from groceries.models import *
from healthandbeauty.models import *
from homeandoffice.models import *
from otherproducts.models import *
from phoneandtablet.models import *
from sporting.models import *
from tvandaudio.models import *  


class BaseFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        fields = ['search']

    def filter_search(self, queryset, name, value):
        words = value.split()
        query = Q()
        for word in words:
            query |= (
                Q(type__name__icontains=word) |
                Q(category__name__icontains=word) |
                Q(subcategory__name__icontains=word) |
                Q(region__name__icontains=word) |
                Q(region__county__name__icontains=word) |
                Q(region__subcounty__name__icontains=word) |
                # Q(brand__name__icontains=word) |
                Q(title__icontains=word)
            )
        return queryset.filter(query)
            
    

class ApplianceFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Appliance

class BabyProductFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = BabyProduct

class FashionFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Fashion

class ComputingFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Computing

class GamingFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Gaming

class GroceryFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Grocery

class Health_BeautyFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Health_Beauty

class Home_OfficeFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Home_Office

class Other_ProductFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Other_Product

class Phone_TabletFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Phone_Tablet

class Sport_GoodingFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Sport_Gooding

class Tv_AudioFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Tv_Audio





