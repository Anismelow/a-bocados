from rest_framework import routers
from .views import IngredientesViewSet
from django.urls import path, include


# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'ingredientes', IngredientesViewSet, basename='ingredientes')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
]