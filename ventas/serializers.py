from rest_framework import serializers
from .models import Venta
from recetas.serializers import RecetaSerializer


class VentaSerializer(serializers.ModelSerializer):
    total_venta = serializers.SerializerMethodField()
    sub_total = serializers.SerializerMethodField()
    productos_vendidos = RecetaSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['nombre_cliente', 'fecha_venta', 'hora_venta', 'horas_trabajadas', 
                  'productos_vendidos', 'costo_empaque', 'costo_decoracion','sub_total', 'total_venta']

    def get_total_venta(self, obj):
        return obj.calcular_total_venta()
    
    def get_sub_total(self, obj):
        return obj.calcular_subtotal()

