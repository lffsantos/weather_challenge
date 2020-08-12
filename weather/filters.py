import django_filters

from weather.models import City


class CityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = City
        fields = ['country', 'state', 'code', 'name']
