from django.urls import path
from .views import *

#urlpatterns = [
    #path('inicio/, inicio, name="inicio")
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('index/', index, name='index'),
    path('mascotas/', mascotas, name='mascotas'),

    path('propietarios/', propietarios, name='propietarios'),
    path('propietariosFormulario/', propietariosFormulario, name='propietariosFormulario'),
    path('listarPropietarios/', listarPropietarios, name='listarPropietarios'),
    path('editarPropietarios/<id>', editarPropietario, name='editarPropietario'),
    path('eliminarPropietario/<id>', eliminarPropietario, name='eliminarPropietario'),

    path('mascotasFormulario/', mascotasFormulario, name='mascotasFormulario'),
    path('listarMascotas/', listarMascotas, name='listarMascotas'),
    path('editarMascota/<id>', editarMascota, name='editarMascota'),
    path('eliminarMascota/<id>', eliminarMascota, name='eliminarMascota'),
    path('mascotasBuscar/', mascotasBuscar, name='mascotasBuscar'),
    path('buscas_mascota/', buscar_mascota, name='buscar_mascota'),
]
