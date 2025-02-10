from django.db import models

class Dato(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    ph = models.FloatField()
    temperatura = models.FloatField()
    turbidez = models.FloatField()
    tds = models.FloatField()
    co2 = models.FloatField()
    ejecucion = models.IntegerField()
    
    def __str__(self):
        return f'{self.fecha}-{self.hora}-{self.usuario}'