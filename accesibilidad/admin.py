from django.contrib import admin
from .models import RecursoAccesibilidad, SolicitudAcceso

@admin.register(RecursoAccesibilidad)
class RecursoAccesibilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'ubicacion', 'cantidad', 'estado', 'necesita_mantenimiento')
    list_filter = ('tipo', 'estado', 'fecha_adquisicion')
    search_fields = ('nombre', 'descripcion', 'ubicacion')
    date_hierarchy = 'fecha_adquisicion'
    ordering = ('nombre',)

@admin.register(SolicitudAcceso)
class SolicitudAccesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'recurso', 'fecha_solicitud', 'estado')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('usuario__username', 'recurso__nombre', 'motivo')
    date_hierarchy = 'fecha_solicitud'