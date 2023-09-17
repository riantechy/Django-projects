# appliances/filters.py
import django_filters
from django.db.models import Q

class BaseFilter(django_filters.FilterSet):
    search = django_filters.Filter(method='filter_search')

    class Meta:
        fields = ['search']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(type__name__icontains=value) |
            Q(category__name__icontains=value) |
            Q(subcategory__name__icontains=value) |
            Q(title__icontains=value) |
            Q(slug__icontains=value)
        )
from beauty.models import *
from cateringandevent.models import *
from cleaning.models import *
from computerandit.models import *
from mechanic.models import *
from transportation.models import *
 

class BeautyFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Beauty

class Catering_EventFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Catering_Event

class CleaningFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Cleaning

class Computer_ItFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Computer_It

class MechanicFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Mechanic

class TransportFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Transport
