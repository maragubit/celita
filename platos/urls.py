from .views import *
from django.urls import path
urlpatterns=[
    path("/editar/<int:pk>",editar_plato,name="editar_plato"),
    path("/eliminar/<int:pk>",eliminar_plato,name="eliminar_plato"),
    path("/anadir/<int:pk>",anadir_plato,name="anadir_plato"),
     
]