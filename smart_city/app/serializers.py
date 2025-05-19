from rest_framework import serializers
from .models import * 


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = '__all__'

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields ='__all__'