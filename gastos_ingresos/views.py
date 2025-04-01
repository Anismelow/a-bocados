from rest_framework import viewsets
from .models import Gastos,Ingresos
from .serializers import GastosSerializer,IngresosSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer
    
class IngresosViewSet(viewsets.ModelViewSet):
    queryset = Ingresos.objects.all()
    serializer_class = IngresosSerializer
    
