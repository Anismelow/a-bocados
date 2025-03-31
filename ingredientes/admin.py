from django.contrib import admin
from .models import Ingredientes
from django.core.exceptions import ValidationError


# Register your models here.

@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_compra', 'unidad','precio_compra', 'distribuidor','precio_unitario')
    list_editable = ('cantidad_compra', 'precio_compra')
    list_per_page = 10
    search_fields = ('nombre',) 
    list_filter = ('distribuidor',)
    ordering = ('nombre',)
    
    
   
   
    
    