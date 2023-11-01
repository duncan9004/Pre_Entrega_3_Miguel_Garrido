from django.urls import path
from inicio.views import inicio
from . import views

urlpatterns=[
    path('', inicio,name='inicio'),
   
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('lista_pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('buscar/', views.buscar, name='buscar'),
]