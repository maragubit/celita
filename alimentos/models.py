from django.db import models

# Create your models here.
class Alimentos(models.Model):
    CAT_CHOICES=(("1","verduras"),("2","frutas"),("3","farináceos"),("4","lácteos"),("5","grasas"))
    nombre=models.CharField(max_length=100)
    categoria=models.CharField(max_length=5, choices=CAT_CHOICES, default='1')
    racion=models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
            return self.nombre
    
    class Meta():
        ordering=['nombre']