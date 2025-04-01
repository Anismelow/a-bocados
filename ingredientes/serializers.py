from rest_framework import serializers
from .models import Ingredientes

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'
        ref_name = "IngredientesSerializerFromIngredientesApp"  # Nombre único

