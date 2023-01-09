import django_filters
from .models import *

class IlanFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    metrekare=django_filters.RangeFilter()
    class Meta:
        model = Ilan
        fields={'name','sehir','price','tip','boyut','metrekare'}