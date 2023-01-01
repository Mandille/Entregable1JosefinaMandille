from django.db import models

# Create your models here.

class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()
    documento = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    numeroRegistro = ()
    vacunas = models.CharField(max_length=30)
    antiparasitarios = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} - {self.numeroRegistro}'  

class Vivienda(models.Model):
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.calle} - {self.numero}'  

