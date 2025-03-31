from django.db import models

# Create your models here.
class Ingredientes(models.Model):
    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unidad = models.CharField(max_length=20, choices=[('g', 'gramos'), ('ml', 'mililitros'), ('lt', 'litro'), ('unidad', 'unidad'), ('kg', 'kilogramos')])
    distribuidor = models.CharField(max_length=250, blank=True, null=True)

    @property
    def precio_unitario(self):
        if not self.cantidad_compra or not self.precio_compra:
            return None
        if self.unidad == "kg":
            calcular_a_gramos =self.cantidad_compra * 1000
            return self.precio_compra / calcular_a_gramos
        elif self.unidad == "ml":
            return self.precio_compra / self.cantidad_compra
        elif self.unidad == "lt":
            calcular_a_mililitros = self.cantidad_compra * 1000
            return self.precio_compra / calcular_a_mililitros
        elif self.unidad == "unidad":
            return self.precio_compra / self.cantidad_compra
        elif self.unidad == "g":
            return self.precio_compra / self.cantidad_compra
        else:
            raise ValueError("Unidad no válida.")

    def __str__(self):
        return f"{self.nombre} - {self.cantidad_compra} {self.unidad} - {self.precio_compra} € - {self.distribuidor}"