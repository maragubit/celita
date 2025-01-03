from django.db import models
from ingredientes.models import Ingredientes
import datetime
from django.db.models import Sum
import os

# Create your models here.
hoy=datetime.datetime.now()
hoy=hoy.date()
class Recetas(models.Model):
    nombre=models.CharField(max_length=50)
    ingredientes=models.ManyToManyField(Ingredientes, related_name="recetas")
    fecha=models.DateField(default=hoy)
    observaciones=models.TextField(max_length=300, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/',blank=True,null=True)

    def raciones(self):
        ingredientes = self.ingredientes.all()
        raciones = 0
        if ingredientes:
            for ingrediente in ingredientes:
                racion = ingrediente.raciones()
                if racion is not None:  # Validación adicional
                    raciones += racion
        return raciones

    
    def total (self):
        total=self.ingredientes.aggregate(total=Sum('cantidad'))['total'] or 0
        return total
    
    def peso_racion(self):
        if self.raciones()==0:
            return 0
        return round((self.total()/self.raciones()),2)
    
    def __str__(self):
        # return (f"{self.nombre} ({self.total()} g), {self.raciones()} raciones")
        return (f"{self.nombre}")
    
    def delete(self, *args, **kwargs):
        # Si existe una imagen asociada a la receta, eliminarla del sistema de archivos
        if self.imagen:
            # Eliminar el archivo de la imagen de la carpeta de medios
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        for ingrediente in self.ingredientes.all():
            ingrediente.delete()
        
        # Llamar al método delete original para eliminar la instancia de la base de datos
        super().delete(*args, **kwargs)
    
    class Meta():
        ordering=['-id']