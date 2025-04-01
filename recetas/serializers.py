from rest_framework import serializers
from .models import Ingredientes,Receta,RecetaIngrediente

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'
        ref_name = "IngredientesSerializerFromRecetasApp"  # Nombre único
        
class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredientesSerializer(many=True, read_only=True)

    class Meta:
        model = Receta
        fields = '__all__'
        read_only_fields = ('ingredientes',)

class RecetaIngredienteSerializer(serializers.ModelSerializer):
    receta = RecetaSerializer(read_only=True)
    ingrediente = IngredientesSerializer(read_only=True)

    class Meta:
        model = RecetaIngrediente
        fields = '__all__'
        read_only_fields = ('receta', 'ingrediente')