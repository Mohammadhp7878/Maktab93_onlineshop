import django_filters
from . import models

class ProductFilter(django_filters.FilterSet):
    is_available = django_filters.BooleanFilter(
        method='check_availability',
        label='is available'
    )
    class Meta:
        model = models.Product
        fields = {
            'categories' : ['exact'],
            'price': ['lte', 'gte'],
            'inventory': ['exact', 'gt']
        }
        
    def check_availability(self, queryset, name, value):
        if value:
            queryset = queryset.filter(inventory__gt=0)
        return queryset        