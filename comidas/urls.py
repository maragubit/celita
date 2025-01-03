from .views import *
from django.urls import path
urlpatterns=[
    path("",index,name="comidas_index"),
    path("/nueva",nueva_comida,name="nueva_comida"),
    path("/buscar",buscar_comida,name="buscar_comida"),
    path("/editar/<int:pk>",editar_comida,name="editar_comida"),
    path("/eliminar/<int:pk>",eliminar_comida,name="eliminar_comida"),
    
]