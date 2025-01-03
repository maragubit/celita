from django.urls import path
from .views import *

urlpatterns = [
    path('', list, name="recetas_list"),
    path('crear', receta_crear, name="recetas_crear"),
    path("/ver/<int:pk>",receta_view,name="receta"),
    path("/borrar/<int:pk>",borrar_receta,name="borrar_receta"),
    path("/editar/<int:pk>",editar_receta,name="editar_receta")
]