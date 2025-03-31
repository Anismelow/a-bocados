from django.contrib import admin
from .models import Receta, RecetaIngrediente
from ingredientes.models import Ingredientes  # Asegúrate de importar el modelo correctamente

class RecetaIngredienteInline(admin.TabularInline):  
    model = RecetaIngrediente
    extra = 1  # Permite agregar ingredientes directamente en la receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porciones', 'precio_base')  
    search_fields = ('nombre',)
    inlines = [RecetaIngredienteInline]

    def precio_base(self, obj):
        return f"{obj.calcular_precio_base()} €"  # Mostramos el precio con formato
    precio_base.short_description = "Precio Base"


@admin.register(RecetaIngrediente)
class RecetaIngredienteAdmin(admin.ModelAdmin):
    list_display = ('receta', 'ingrediente', 'cantidad', 'unidad')
    list_filter = ('unidad',)
    search_fields = ('receta__nombre', 'ingrediente__nombre')