from django.db import models
from ckeditor.fields import RichTextField

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField( )
    

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField()
    costo = models.IntegerField()
