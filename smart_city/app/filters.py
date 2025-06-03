import django_filters
from .models import Sensores, Historico, Ambientes


# filter_backends = [DjangoFilterBackend]
# filterset_class = AmbienteFilter --> Na View
class SensorFIlter(django_filters.FilterSet):
    tipo_sensor = django_filters.CharFilter(field_name='sensor', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    class Meta:
        model = Sensores
        fields = ['sensor', 'status']

class AmbienteFilter(django_filters.FilterSet):
    sig = django_filters.NumberFilter(field_name='sig', lookup_expr='iexact')
    ni = django_filters.CharFilter(field_name='ni', lookup_expr='iexact')
    class Meta:
        model = Ambientes
        fields = ['sig', 'ni']

class HistoricoFilter(django_filters.FilterSet):
    timestamp = django_filters.DateTimeFilter(field_name='timestamp', method='filter_exact_datetime')
    class Meta:

        model = Historico
        fields = ['timestamp']

    def filter_exact_datetime(self, queryset, name, value):
        from datetime import timedelta

        # Tolerância de 1 segundo (ajuste se quiser mais precisão)
        delta = timedelta(seconds=1)
        return queryset.filter(timestamp__gte=value - delta, timestamp__lte=value + delta)