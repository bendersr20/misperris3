from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Persona, Estado, Comuna, Regiones, Vivienda, Mascota


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_mas', 'nom_mas', 'tamano_mas','peso_mas','color_mas','fecha_res','descripcion','estado')
    list_filter = ('estado',)
    ordering = ('id_mas',)
    search_fields = ('nom_mas',)


class RegistroPersona(admin.ModelAdmin):
    list_display = ('rut', 'email', 'nombre','fec_nac','fono','region','comuna','tp_vivienda')
    list_filter = ('rut',)
    ordering = ('rut',)
    search_fields = ('nombre',)

admin.site.register(Persona)
admin.site.register(Estado)
admin.site.register(Comuna)
admin.site.register(Regiones)
admin.site.register(Vivienda)
admin.site.register(Mascota)