from django.db import models
from ingredientes.models import Ingredientes  # Asegúrate de que el modelo esté bien nombrado

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    preparacion = models.TextField(blank=True, null=True)
    tiempo_coccion = models.IntegerField(blank=True, null=True)
    porciones = models.CharField(max_length=250, blank=True, null=True)
    
    # Relación ManyToMany con el modelo Ingrediente a través de RecetaIngrediente
    ingredientes = models.ManyToManyField(Ingredientes, through='RecetaIngrediente')

    def calcular_precio_base(self):
        precio_total = 0
        for ri in self.ingredientes_relacionados.all():  # Usamos el related_name 'ingredientes_relacionados'
            if ri.ingrediente.precio_unitario:
                precio_total += (ri.ingrediente.precio_unitario * ri.cantidad)
        return round(precio_total, 2)  # Redondeamos el resultado a 2 decimales

    def __str__(self):
        return f"{self.nombre} - {self.porciones} porciones - Precio Base: {self.calcular_precio_base()}€"
    

class RecetaIngrediente(models.Model):  
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name="ingredientes_relacionados")
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unidad = models.CharField(
        max_length=20, 
        choices=[
            ('g', 'gramos'), 
            ('ml', 'mililitros'), 
            ('lt', 'litro'), 
            ('unidad', 'unidad'), 
            ('kg', 'kilogramos')
        ]
    )
    
    def __str__(self):
        return f"{self.ingrediente.nombre}: {self.cantidad} {self.unidad} en {self.receta.nombre}"
