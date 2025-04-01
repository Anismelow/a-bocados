from django.db import models
from recetas.models import Receta
from django.utils import timezone
from decimal import Decimal  
from gastos_ingresos.models import Ingresos



PRECIOS_LUZ = {
    "00": 0.1319, "01": 0.1187, "02": 0.1165, "03": 0.1037, "04": 0.1048,
    "05": 0.1109, "06": 0.1260, "07": 0.2061, "08": 0.2441, "09": 0.1530,
    "10": 0.1591, "11": 0.1226, "12": 0.1162, "13": 0.1135, "14": 0.0485,
    "15": 0.0493, "16": 0.0495, "17": 0.0496, "18": 0.1363, "19": 0.1816,
    "20": 0.2461, "21": 0.2555, "22": 0.1494, "23": 0.1225,
}


class Venta(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_venta = models.DateField(default=timezone.now)
    hora_venta = models.TimeField(default=timezone.now)
    horas_trabajadas = models.PositiveIntegerField(default=1)  # Horas trabajadas
    productos_vendidos = models.ManyToManyField(Receta, related_name='ventas')
    costo_empaque = models.DecimalField(max_digits=6, decimal_places=2, default=0) 
    costo_decoracion = models.DecimalField(max_digits=6, decimal_places=2, default=0)  

    def calcular_subtotal(self):
        subtotal = 0

        # 1️⃣ Sumar el precio base de las recetas vendidas
        for receta in self.productos_vendidos.all():
            subtotal += receta.calcular_precio_base()

        # 2️⃣ Costo de luz según las horas trabajadas
        hora_inicio = int(self.hora_venta.strftime("%H"))
        for i in range(self.horas_trabajadas):
            hora_actual = str((hora_inicio + i) % 24).zfill(2)
            costo_luz = Decimal(str(PRECIOS_LUZ.get(hora_actual, 0)))  
            subtotal += costo_luz

        # 3️⃣ Costo de mano de obra (10€ por cada hora trabajada)
        subtotal += self.horas_trabajadas * 10

        # 4️⃣ Sumar costos de empaque y decoraciones
        subtotal += self.costo_empaque
        subtotal += self.costo_decoracion

        return subtotal

    def calcular_total_venta(self):
        subtotal = self.calcular_subtotal()
        return int(subtotal * Decimal("1.30"))
    
   
        

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha_venta} - Total: {self.calcular_total_venta()}€"
