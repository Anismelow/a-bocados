from django.shortcuts import render
from .models import Receta,RecetaIngrediente
from rest_framework import viewsets
from .serializers import  RecetaSerializer, RecetaIngredienteSerializer

# Create your views here.


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    
class RecetaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = RecetaIngrediente.objects.all()
    serializer_class = RecetaIngredienteSerializer
    

