from django.contrib import admin
from .models import Persona, Mascota, Vivienda

# Register your models here.

admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(Vivienda)