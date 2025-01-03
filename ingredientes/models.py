from django.db import models
from alimentos.models import Alimentos

# Create your models here.
class Ingredientes(models.Model):
    alimento=models.ForeignKey(Alimentos,related_name='ingredientes',on_delete=models.CASCADE)
    cantidad=models.DecimalField(max_digits=6, decimal_places=2)
    
    def raciones(self):
        if self.alimento.racion==0:
            return 0
        return round((self.cantidad/self.alimento.racion),2)
    
    def __str__(self):
        return (f"{self.alimento} : {self.cantidad}")