from django.shortcuts import render
from .models import Ingredientes
from recetas.models import Recetas
from alimentos.models import Alimentos
import json

# Create your views here.

def editar_ingrediente(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs["id_receta"])
    
    alimentos=Alimentos.objects.all()
    if request.method=="POST":
        
        for indice,ingrediente in enumerate(receta.ingredientes.all()):
            ingrediente.alimento=Alimentos.objects.get(id=int(request.POST["ingredientes"+str(indice)]))
            ingrediente.cantidad=int(request.POST["cantidad"+str(indice)])
            ingrediente.save()
            return render(request,"recetas/editar.html",{"object":receta})
        
    contexto={
        "alimentos":alimentos,
        "receta":receta
    }
    return render (request,"ingredientes/editar.html",contexto)


def borrar_ingrediente(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs["id_receta"])
    Ingredientes.objects.get(id=kwargs["pk"]).delete()
   
    return render(request,"recetas/editar.html",{"object":receta})

def mas_ingredientes(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs["id_receta"])
    alimentos=Alimentos.objects.all()
    ingredientesList=[]
    if request.method=="POST":
        for ingrediente,cantidad in json.loads(request.POST["diccionario"]).items():#recorremos dicc json con alimento id y cantidad
            alimento=Alimentos.objects.get(id=int(ingrediente))
            i=Ingredientes(alimento=alimento,cantidad=float(cantidad))
            i.save()#creamos el ingrediente
            ingredientesList.append(i)
        receta.ingredientes.add(*ingredientesList)
        receta.save()
        return render(request,"recetas/receta.html",{"object":receta})
    return render (request,"ingredientes/mas_ingredientes.html",{"object":receta,"alimentos":alimentos})