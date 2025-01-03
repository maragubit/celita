from .views import *
from django.urls import path
urlpatterns=[
    path("/editar/ingredientes/<int:id_receta>",editar_ingrediente,name="editar_ingrediente"),
    path("/borrar/<int:pk>/<int:id_receta>",borrar_ingrediente,name="borrar_ingrediente"),
    path("/agregar/ingredientes/<int:id_receta>",mas_ingredientes,name="agregar_ingredientes"),
]