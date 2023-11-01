from django.urls import path
from inicio.views import inicio,paletas,crear_paleta
from . import views

urlpatterns=[
    path('', inicio,name='inicio'),
    path('paletas/',paletas,name='paletas'),
    path('paletas/crear/',crear_paleta,name='crear_paleta'),
   
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('lista_pacientes/', views.lista_pacientes, name='lista_pacientes'),
]