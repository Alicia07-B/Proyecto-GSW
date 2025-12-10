from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('numero_inventario', 'descripcion', 'precio_adquisicion', 'usuario_responsable')
    search_fields = ('numero_inventario', 'descripcion')
    list_filter = ('usuario_responsable',)