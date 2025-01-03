from django.shortcuts import render,redirect
from .models import Comidas
from dietas.models import Dietas
from recetas.models import Recetas
from platos.models import Platos
import datetime as dt
from dateutil.relativedelta import relativedelta  # type: ignore
from datetime import datetime
# Create your views here.

def index(request):
    
    dieta=Dietas.objects.get(activada=True)
    hoy=dt.date.today()
    """Dias de la semana de lunes a domingo"""
    lunes=hoy-relativedelta(days=+hoy.weekday())
    martes=lunes+relativedelta(days=+1)
    miercoles=lunes+relativedelta(days=+2)
    jueves=lunes+relativedelta(days=+3)
    viernes=miercoles=lunes+relativedelta(days=+4)
    sabado=miercoles=lunes+relativedelta(days=+5)
    domingo=miercoles=lunes+relativedelta(days=+6)
    
    
    comidas=Comidas.objects.filter(fecha__gte=lunes,fecha__lte=hoy).order_by("fecha")#comidas entre el lunes de esta semana y hoy

    """Comidas de lunes a domingo"""
    comidas_lunes=comidas.filter(fecha=lunes)
    comidas_martes=comidas.filter(fecha=martes)
    comidas_miercoles=comidas.filter(fecha=miercoles)
    comidas_jueves=comidas.filter(fecha=jueves)
    comidas_viernes=comidas.filter(fecha=viernes)
    comidas_sabado=comidas.filter(fecha=sabado)
    comidas_domingo=comidas.filter(fecha=domingo)
    
    """Contexto"""
    
    contexto={
        "hoy":hoy,
        "domingo":domingo,
        "lunes":lunes,
        "comida_lunes":comidas_lunes,
        "comida_martes":comidas_martes,
        "comida_miercoles":comidas_miercoles,
        "comida_jueves":comidas_jueves,
        "comida_viernes":comidas_viernes,
        "comida_sabado":comidas_sabado,
        "comida_domingo":comidas_domingo,
        "dieta":dieta,
        "rango":range(1,7),



    }
    return render(request,"comidas/index.html",contexto)

def nueva_comida(request):
    recetas=Recetas.objects.all()
    if request.method=="POST":
        receta=Recetas.objects.get(id=int(request.POST["recetas"]))
        cantidad=float(request.POST["cantidad"])
        fecha=request.POST["fecha"]
        momento=request.POST["momento"]
        dieta=Dietas.objects.get(activada=True)
        plato=Platos(receta=receta,cantidad=cantidad)
        plato.save()
        comida=Comidas.objects.filter(momento=int(momento),fecha=fecha).last()
        if comida:
            comida.platos.add(plato)
        else:    
            comida=Comidas(momento=int(momento),fecha=fecha,dieta=dieta)
            comida.save()
            comida.platos.add(plato)
            comida.save()

        return redirect('comidas_index')

    contexto={
        "recetas":recetas,
    }
    return render(request,"comidas/nueva.html",contexto)


def buscar_comida(request):
    texto=""
    if request.method=="POST":
        fecha=request.POST['fecha']
        momento=request.POST['momento']
        comida=Comidas.objects.filter(fecha=fecha,momento=momento).last()
        
        if comida:
            return redirect ('editar_comida',pk=comida.id)
        else:
            texto="No se ha encontrado ninguna comida"
        
    return render (request,"comidas/buscar.html",{"texto":texto})

def editar_comida(request,**kwargs):
    comida=Comidas.objects.get(id=kwargs['pk'])
    if request.method=="POST":
        comida.momento=int(request.POST["momento"])
        fecha_str=request.POST["fecha"]
        comida.fecha=datetime.strptime(fecha_str, "%Y-%m-%d").date()
        comida.save()
    contexto={
        "comida":comida
    }
    return render(request, "comidas/editar.html",contexto)

def eliminar_comida(request,**kwargs):
    comida=Comidas.objects.get(id=kwargs['pk'])
    for plato in comida.platos.all():
        plato.delete()
    comida.delete()
    return redirect('comidas_index')