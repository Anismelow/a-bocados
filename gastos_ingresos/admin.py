from django.contrib import admin
from .models import Gastos, Ingresos
from django.db.models import Sum
 
@admin.register(Ingresos)
class IngresosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto', 'fecha', 'categoria')
    search_fields = ('nombre', 'categoria')
    list_filter = ('fecha', 'categoria')
    ordering = ('-fecha',)
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        total = Ingresos.objects.aggregate(total=Sum('monto'))['total'] or 0
        extra_context['total_ingresos'] = total
        return super().changelist_view(request, extra_context=extra_context)
    
    def total_ingresos(self, request):
        total = Ingresos.objects.aggregate(Sum('monto'))['monto__sum']
        return total if total else 0
    

@admin.register(Gastos)
class GastosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto', 'fecha', 'categoria')
    search_fields = ('nombre', 'categoria')
    list_filter = ('fecha', 'categoria')
    ordering = ('-fecha',)
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        total = Gastos.objects.aggregate(total=Sum('monto'))['total'] or 0
        extra_context['total_gastos'] = total
        return super().changelist_view(request, extra_context=extra_context)
    
    def total_gastos(self, request):
        total = Gastos.objects.aggregate(Sum('monto'))['monto__sum']
        return total if total else 0
    