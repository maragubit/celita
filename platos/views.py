from django.shortcuts import render,redirect
from .models import Platos
from comidas.models import Comidas

from recetas.models import Recetas
import datetime as dt
from dateutil.relativedelta import relativedelta  # type: ignore
# Create your views here.
def editar_plato (request,**kwargs):
    plato=Platos.objects.get(id=kwargs['pk'])
    if request.method=="POST":
        plato.cantidad=float(request.POST['cantidad'])
        plato.save()
        return redirect ("comidas_index")
    return render (request,"platos/editar.html",{"plato":plato})

def eliminar_plato (request,**kwargs):
    plato=Platos.objects.get(id=kwargs['pk'])
    plato.delete()
    return redirect ("comidas_index")


def anadir_plato (request,**kwargs):
    comida=Comidas.objects.get(id=kwargs['pk'])
    recetas=Recetas.objects.all()
    if request.method=="POST":
        receta=Recetas.objects.get(id=int(request.POST["recetas"]))
        cantidad=float(request.POST["cantidad"])
        plato=Platos(receta=receta,cantidad=cantidad)
        plato.save()
        comida.platos.add(plato)
        comida.save()
        return redirect ("comidas_index")
    return render (request,"platos/anadir.html",{"recetas":recetas})
    
    
