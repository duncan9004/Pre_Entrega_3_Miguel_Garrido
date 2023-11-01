from django.db import models

class Paleta(models.Model):
    marca=models.CharField(max_length=30)
    descripcion=models.TextField()
    anio=models.IntegerField()


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.IntegerField()
