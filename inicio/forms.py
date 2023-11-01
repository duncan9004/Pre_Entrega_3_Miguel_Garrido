from django import forms
from .models import Paciente, Cita, Tratamiento

class PacienteForm(forms.Form):
    class Meta:
        model = Paciente
        fields = '__all__'

class CitaForm(forms.Form):
    class Meta:
        model = Cita
        fields = '__all__'

class TratamientoForm(forms.Form):
    class Meta:
        model = Tratamiento
        fields = '__all__'
