from rest_framework import routers
from django.urls import path, include
from .views import GastosViewSet,IngresosViewSet


router = routers.DefaultRouter()
router.register(r'gastos', GastosViewSet, basename='gastos')
router.register(r'ingresos', IngresosViewSet, basename='ingresos')

urlpatterns = [
    path('', include(router.urls)),
]