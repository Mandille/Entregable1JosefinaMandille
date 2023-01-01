from django.shortcuts import render
from .models import Persona, Mascota, Vivienda
from django.http import HttpResponse
from .forms import PersonaForm, MascotaForm, ViviendaForm

# Create your views here.

def inicio(request):
    return render (request, "AppProyecto/inicio.html")

def index(request):
    return render (request, "AppProyecto/index.html")

def propietarios(request):
    return render (request, "AppProyecto/propietarios.html")

def mascotas(request):
    return render (request, "AppProyecto/mascotas.html")

def propietariosFormulario (request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            fechaNacimiento = informacion["fechaNacimiento"]
            edad = informacion["edad"]
            documento = informacion["documento"]
            telefono = informacion["telefono"]
            propietario = Persona(nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, edad=edad, documento=documento, telefono=telefono)
            propietario.save()
            propietarios = Persona.objects.all()
            return render (request, 'AppProyecto/propietariosLista.html',{"propietarios":propietarios, "parrafo":"Propietario registrado correctamente"})
        else:
            return render (request, 'AppProyecto/propietariosFormulario.html',{"form":form, "mensaje":"Error al registrar propietario"})
    else:
        formulario = PersonaForm()
        return render (request, 'AppProyecto/propietariosFormulario.html',{"form":formulario})

def listarPropietarios(request):
    propietarios = Persona.objects.all()
    return render (request, 'AppProyecto/propietariosLista.html',{"propietarios":propietarios})

def editarPropietario(request, id):
    propietario = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            propietario.nombre = info["nombre"]
            propietario.apellido = info["apellido"]
            propietario.fechaNacimiento = info["fechaNacimiento"]
            propietario.edad = info["edad"]
            propietario.documento = info["documento"]
            propietario.telefono = info["telefono"]
            propietario.save()
            propietarios = Persona.objects.all()
            return render (request, 'AppProyecto/propietarioLista.html',{"propietarios":propietarios, "parrafo":"Propietario editado correctamente"})
        pass
    else:
        form= PersonaForm(initial={"nombre":propietario.nombre, "apellido":propietario.apellido, "fechaNacimiento":propietario.fechaNacimiento, "edad":propietario.edad, "documento":propietario.documento, "telefono":propietario.telefono})
        return render (request, 'AppProyecto/editarPropietario.html',{"form":form, "propietario":propietario})

def eliminarPropietario(request, id):
    propietario = Persona.objects.get(id=id)
    propietario.delete()
    jugadores = Persona.objects.all()
    return render (request, 'AppProyecto/propietarioLista.html',{"propietarios":propietarios, "parrafo":"Propietario eliminado correctamente"})


def mascotasFormulario (request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            raza = informacion["raza"]
            edad = informacion["edad"]
            numeroRegistro = informacion["numeroRegistro"]
            vacunas = informacion["vacunas"]
            antiparasitarios = informacion["antiparasitarios"]
            mascota = Mascota(nombre=nombre, raza=raza, edad=edad, numeroRegistro=numeroRegistro, vacunas=vacunas, antiparasitarios=antiparasitarios)
            mascota.save()
            mascotas = Mascota.objects.all()
            return render (request, 'AppProyecto/mascotasLista.html',{"mascotas":mascotas, "parrafo":"Mascota registrada correctamente"})
        else:
            return render (request, 'AppProyecto/mascotasFormulario.html',{"form":form, "mensaje":"Error al registrar mascota"})
    else:
        formulario = MascotaForm()
        return render (request, 'AppProyecto/mascotasFormulario.html',{"form":formulario})

def listarMascotas(request):
    mascotas = Mascota.objects.all()
    return render (request, 'AppProyecto/mascotasLista.html',{"mascotas":mascotas})

def editarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            mascota.nombre = info["nombre"]
            mascota.raza = info["raza"]
            mascota.edad = info["edad"]
            mascota.numeroRegistro = info["numeroRegistro"]
            mascota.vacunas = info["vacunas"]
            mascota.antiparasitarios = info["antiparasitarios"]
            mascota.save()
            mascotas = Mascota.objects.all()
            return render (request, 'AppProyecto/mascotasLista.html',{"mascotas":mascotas, "parrafo":"Mascota editada correctamente"})
        pass
    else:
        form= MascotaForm(initial={"nombre":mascota.nombre, "raza":mascota.raza, "edad":mascota.edad, "numeroRegistro":mascota.numero_de_registro, "vacunas":mascota.vacunas, "antiparasitarios":mascota.antiparasitarios})
        return render (request, 'AppProyecto/editarMascotas.html',{"form":form, "mascota":mascota})

def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    mascotas = Mascota.objects.all()
    return render (request, 'AppProyecto/mascotasLista.html',{"mascotas":mascotas, "parrafo":"Mascota eliminada correctamente"})

def mascotasBuscar(request):
    return render (request, 'AppProyecto/mascotasBuscar.html')

def buscar_mascota(request):
    numeroRegistro=request.GET["numeroRegistro"]
    if numeroRegistro != "":
        mascotas = Mascota.objects.filter(numeroRegistro=numeroRegistro)
        return render (request, 'AppProyecto/mascotasLista.html',{"mascotas":mascotas, "parrafo":"Resultado de la busqueda"})
    else:
        return render (request, 'AppProyecto/mascotasBuscar.html',{"mensaje":"Debe ingresar un numero de registro"})



