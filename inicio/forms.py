from django import forms
from .models import Paciente, Cita, Tratamiento
from ckeditor.fields import RichTextFormField

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields ='__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class BusquedaForm(forms.Form):
    termino = forms.CharField(max_length=100, required=False, label='Buscar')