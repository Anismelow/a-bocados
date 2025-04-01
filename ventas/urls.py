from rest_framework import routers
from django.urls import path, include
from .views import VentaViewSet

router = routers.DefaultRouter()
router.register(r'ventas', VentaViewSet, basename='ventas')

urlpatterns = [
    path('', include(router.urls)),
]
