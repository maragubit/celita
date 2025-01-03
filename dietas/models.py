from django.db import models
import datetime as dt

# Create your models here.
hoy=dt.date.today()
class Dietas(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField(default=hoy)
    desayuno=models.IntegerField()
    media_manana=models.IntegerField( verbose_name="media mañana")
    almuerzo=models.IntegerField()
    merienda=models.IntegerField()
    cena=models.IntegerField()
    antes_dormir=models.IntegerField(verbose_name="antes de dormir")
    observaciones=models.TextField(max_length=300,null=True,blank=True)
    activada=models.BooleanField(default=False)

    def __str__(self):
        if self.activada:
            return (f"{self.nombre}: raciones: D {self.desayuno}/ MM {self.media_manana}/ A {self.almuerzo}/ M {self.merienda}/ C {self.cena}/ AD {self.antes_dormir} ACTIVADA")
    
        return (f"{self.nombre}: raciones: D {self.desayuno}/ MM {self.media_manana}/ A {self.almuerzo}/ M {self.merienda}/ C {self.cena}/ AD {self.antes_dormir} ")
    
    def save(self, *args, **kwargs):
        if self.activada:  # Si esta dieta está activada
            # Desactivar todas las demás dietas
            dietas = Dietas.objects.exclude(pk=self.pk)  # Excluir la actual por su PK
            for dieta in dietas:
                dieta.activada = False
                dieta.save()
        
        # Guardar la instancia actual
        super().save(*args, **kwargs)