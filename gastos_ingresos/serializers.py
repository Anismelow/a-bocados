from rest_framework import serializers
from .models import Ingresos,Gastos

class IngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresos
        fields = '__all__'
        
class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = '__all__'
        
