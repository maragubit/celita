from django.shortcuts import render
from alimentos.models import Alimentos
import pandas as pd

# Create your views here.
def portada(request):
    """ file_path = './alimentos.xlsx'  # Replace with your file path
    data = pd.read_excel(file_path)
    for indice,dato in enumerate(data.Alimento):
        alimento=Alimentos(nombre=data.Alimento[indice].lower(),racion=data.Peso[indice],categoria=data.Categoria[indice])
        alimento.save() """
    
    return render(request,"core/index.html")

def calculadora(request):
    return render(request,"core/calculadora.html")