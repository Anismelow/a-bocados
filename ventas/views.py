from django.shortcuts import render
from .models import Venta
from .serializers import VentaSerializer
from rest_framework import viewsets


# Create your views here.
class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
