from django.db import models


# Create your models here.
class Gastos(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.monto} - {self.fecha} - {self.categoria} - {self.calcular_total_gastos()}"
    
    def calcular_total_gastos(self):
        return sum(gasto.monto for gasto in Gastos.objects.all())
    
class Ingresos(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)

    def calcular_total_ingresos(self):
        return sum(ingreso.monto for ingreso in Ingresos.objects.all())
    
    def __str__(self):
        return f"{self.nombre} - {self.monto} - {self.fecha} - {self.categoria}  - {self.calcular_total_ingresos()}"
    
   
    
    
    
   
        