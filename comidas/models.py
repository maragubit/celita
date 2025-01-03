from django.db import models
from platos.models import Platos
from dietas.models import Dietas
import datetime as dt
from django.core.exceptions import ValidationError
# Create your models here.
hoy=dt.datetime.now()
class Comidas(models.Model):
    momento_choices=((1,"desayuno"),(2,"media mañana"),(3,"almuerzo"),(4,"merienda"),(5,"cena"),(6,"antes de dormir"))
    platos=models.ManyToManyField(Platos,related_name="comidas")
    momento=models.IntegerField(max_length=10,choices=momento_choices)
    fecha=models.DateField(default=hoy)
    dieta=models.ForeignKey (Dietas,on_delete=models.SET_NULL, related_name="comidas", blank=True, null=True, limit_choices_to={'activada': True})

    def __str__(self):
        return (f"{self.get_momento_display()} : {self.fecha}")
    
    def raciones(self):
        raciones=0
        platos=self.platos.all()
        if platos:
            for plato in platos:
                raciones+=plato.raciones()
        return raciones
    
    """ def save(self, *args, **kwargs):
        comida=Comidas.objects.filter(momento=self.momento,fecha=self.fecha).exclude(self).first()
        if comida:
             platos=self.platos.all()
             comida.platos.add(platos)
             comida.save
        else:
        # Guardar la instancia actual
            super().save(*args, **kwargs) """
