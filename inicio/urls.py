from django.urls import path
from inicio.views import inicio
from . import views
from .views import mostrar_fecha_hora


urlpatterns=[
    path('', inicio,name='inicio'),
   
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('lista_pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('mostrar_pacientes/', views.cita, name='mostrar_cita'),
    path('buscar/', views.buscar, name='buscar'),
    path('sobre_nosotros/',views.sobre_nosotros, name='sobre_nosotros'),
    path('mostrar_fecha_hora/', mostrar_fecha_hora, name='mostrar_fecha_hora'),

]