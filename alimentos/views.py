from django.shortcuts import render
from .models import Alimentos


# Create your views here.

def alimentos(request):
    alimentos=Alimentos.objects.all()
    return render(request,"alimentos/alimentos.html",{"alimentos":alimentos})

