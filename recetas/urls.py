from rest_framework import routers
from django.urls import path, include
from .views import  RecetaViewSet, RecetaIngredienteViewSet


router = routers.DefaultRouter()
router.register(r'recetas', RecetaViewSet, basename='recetas')
router.register(r'receta-ingredientes', RecetaIngredienteViewSet, basename='receta-ingredientes')

urlpatterns = [
    path('', include(router.urls)),
]