from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Venta
from gastos_ingresos.models import Ingresos

@receiver(post_save, sender=Venta)
def crear_ingreso(instance, created, **kwargs):
    if created:
        Ingresos.objects.create(
            nombre=instance.nombre_cliente,
            monto=instance.calcular_total_venta(),
            fecha=instance.fecha_venta,
            categoria="Venta"
        )
        print(f"Se ha creado un ingreso por la venta: {instance.nombre_cliente} - {instance.calcular_total_venta()}")