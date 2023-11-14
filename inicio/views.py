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


    return render(request, 'inicio/buscar_resultados.html', {'resultados': resultados, 'form': form})

def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de pacientes
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'inicio/agregar_paciente.html', {'form': form})


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'inicio/lista_pacientes.html', {'pacientes': pacientes})
 
def sobre_nosotros(request):
    return render(request,'inicio/sobre_nosotros.html')

def cita(request):
    pacientes=Paciente.objects.all()
    return render(request)

def tratamiento(request):
    pacientes=Paciente.objects.all()
    
