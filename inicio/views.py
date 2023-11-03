from django.shortcuts import render,redirect
from inicio.models import Paciente
from .forms import PacienteForm, CitaForm, TratamientoForm,BusquedaForm

def inicio(request):
    
  
    return render(request,"inicio/inicio.html",{})

def buscar(request):
    resultados = None
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data.get('termino')
            resultados = Paciente.objects.filter(nombre__icontains=termino)  
             
    return render(request, 'buscar_resultados.html', {'resultados': resultados, 'form': form})

def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render('inicio/lista_pacientes')  # Redirigir a la lista de pacientes
    else:
        form = PacienteForm()
    return render(request, 'inicio/agregar_paciente.html', {'form': form})


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'inicio/lista_pacientes.htm l', {'pacientes': pacientes})

def cita(request):
    pacientes=Paciente.objects.all()
    return render(request)

def tratamiento(request):
    pacientes=Paciente.objects.all()
