from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50, label='nombre')
    apellido = forms.CharField(max_length=50, label='apellido')
    fechaNacimiento = forms.DateField(label='fechaNacimiento') 
    edad = forms.IntegerField(label='edad')
    documento = forms.IntegerField(label='documento')
    telefono = forms.IntegerField(label='telefono')

class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=30, label='nombre')
    raza = forms.CharField(max_length=30, label='raza')
    edad = forms.IntegerField(label='edad')
    numeroRegistro = forms.IntegerField(label='numeroRegistro')
    vacunas = forms.CharField(max_length=30, label='vacunas')
    antiparasitarios = forms.CharField(max_length=30, label='antiparasitarios')

class ViviendaForm(forms.Form):
    calle = forms.CharField(max_length=30, label='calle')
    numero = forms.IntegerField(label='numero')
