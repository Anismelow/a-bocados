from django.shortcuts import render
from .serializers import IngredientesSerializer
from .models import Ingredientes
from rest_framework import viewsets

# Create your views here.
class IngredientesViewSet(viewsets.ModelViewSet):

    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer
    

