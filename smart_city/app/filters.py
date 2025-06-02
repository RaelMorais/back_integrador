import django_filters
from .models import Sensores, Historico, Ambientes


class SensorFIlter(django_filters.FilterSet):
    tipo_sensor = django_filters.CharFilter(field_name='sensor', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    class Meta:
        model = Sensores
        fields = ['sensor', 'status']

class AmbienteFiltro(django_filters.FilterSet):
    sig = django_filters.NumberFilter(field_name='sig', lookup_expr='exact')
    class Meta:
        model = Ambientes
        fields = ['sig']