import django_filters
from .models import Sensores, Historico, Ambientes
from datetime import timedelta

# filter_backends = [DjangoFilterBackend]
# filterset_class = AmbienteFilter --> Na View

# Filtro para sensor onde busca a field com nome de sensor e procura um valor aproximado --> icontains e status com um valor extado --> iexact
class SensorFIlter(django_filters.FilterSet):
    tipo_sensor = django_filters.CharFilter(field_name='sensor', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    class Meta:
        model = Sensores
        fields = ['sensor', 'status']

# Filtro para ambiente onde busca o exato sig e o exato ni
class AmbienteFilter(django_filters.FilterSet):
    sig = django_filters.NumberFilter(field_name='sig', lookup_expr='iexact')
    ni = django_filters.CharFilter(field_name='ni', lookup_expr='iexact')
    class Meta:
        model = Ambientes
        fields = ['sig', 'ni']

# Filtro para historico 
class HistoricoFilter(django_filters.FilterSet):
    timestamp = django_filters.DateTimeFilter(field_name='timestamp', method='filter_exact_datetime')
    class Meta:

        model = Historico
        fields = ['timestamp']

    # função para buscar a data exata no excel 
    def filter_exact_datetime(self, queryset, name, value):
        # tolerancia de 1 segundo para realizar a busca 
        delta = timedelta(seconds=1)
        return queryset.filter(timestamp__gte=value - delta, timestamp__lte=value + delta)