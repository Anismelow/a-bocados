from django.contrib import admin
from django.contrib import admin
from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha_venta', 'hora_venta', 'horas_trabajadas', 'calcular_subtotal', 'calcular_total_venta','lista_productos')
    list_filter = ('fecha_venta',)
    search_fields = ('nombre_cliente',)
    filter_horizontal = ('productos_vendidos',)
    
    def lista_productos(self, obj):
        return ", ".join([p.nombre for p in obj.productos_vendidos.all()])
    lista_productos.short_description = "Productos Vendidos"

    def calcular_subtotal(self, obj):
        return f"{obj.calcular_subtotal():.2f}€"
    calcular_subtotal.short_description = "Subtotal (€)"

    def calcular_total_venta(self, obj):
        return f"{obj.calcular_total_venta():.2f}€"
    calcular_total_venta.short_description = "Total Venta (€)"

admin.site.register(Venta, VentaAdmin)

