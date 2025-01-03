from django.db import models
from recetas.models import Recetas
# Create your models here.

class Platos(models.Model):
    receta=models.ForeignKey(Recetas, related_name="recetas",on_delete=models.CASCADE)
    cantidad=models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        return (f"{self.cantidad}g de {self.receta}")
    
    def raciones(self):
        return round((self.cantidad*self.receta.raciones()/self.receta.total()),2)