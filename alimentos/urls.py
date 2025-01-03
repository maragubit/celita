from django.urls import path
from .views import *

urlpatterns = [
    path('', alimentos, name="alimentos"),
]