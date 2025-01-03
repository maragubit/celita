from django.shortcuts import render
from .models import Recetas
from ingredientes.models import Ingredientes
from alimentos.models import Alimentos
import json


# Create your views here.

def list(request):
    recetas=Recetas.objects.all()
    return render(request,"recetas/lista.html",{"recetas":recetas})

def receta_view(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs['pk'])
    return render(request,"recetas/receta.html",{"object":receta})

def receta_crear(request):
    alimentos=Alimentos.objects.all()
    recetas=Recetas.objects.all()
    contexto={
        "alimentos":alimentos,
    }
    if request.method=="POST":
        nombre=request.POST["nombre"]
        foto=request.FILES.get('foto')
        if not foto:
            foto = None
        observaciones=request.POST["observaciones"]
        ingredientesList=[]
        for ingrediente,cantidad in json.loads(request.POST["diccionario"]).items():#recorremos dicc json con alimento id y cantidad
            alimento=Alimentos.objects.get(id=int(ingrediente))
            i=Ingredientes(alimento=alimento,cantidad=float(cantidad))
            i.save()#creamos el ingrediente
            ingredientesList.append(i)
        receta=Recetas(nombre=nombre,observaciones=observaciones,imagen=foto)
        receta.save()
        receta.ingredientes.set(ingredientesList)
        receta.save()
           
        return render(request,"recetas/lista.html",{"recetas":recetas})
    
    return render(request,"recetas/crear.html",contexto)


def borrar_receta(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs["pk"])
    receta.delete()
    recetas=Recetas.objects.all()
    return render(request,"recetas/lista.html",{"recetas":recetas})

def editar_receta(request,**kwargs):
    receta=Recetas.objects.get(id=kwargs["pk"])
    if request.method=="POST":
        nombre=request.POST["nombre"]
        observaciones=request.POST["observaciones"]
        foto=request.FILES.get('foto')
        if foto:
            receta.imagen=foto
            receta.save()
        receta.nombre=nombre
        receta.observaciones=observaciones
        receta.save()
        return render(request,"recetas/receta.html",{"object":receta})
    
    return render(request,"recetas/editar.html",{"object":receta})
    