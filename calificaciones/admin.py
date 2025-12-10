from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'nota', 'fecha')
    list_filter = ('materia', 'fecha')
    search_fields = ('estudiante', 'materia')