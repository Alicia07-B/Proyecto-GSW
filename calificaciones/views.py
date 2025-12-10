from django.shortcuts import render
from django.http import HttpResponse # type: ignore

def listar_calificaciones(request):
    return render(request, 'calificaciones/listar_calificaciones.html', {
        'calificaciones': []
    })

def agregar_calificacion(request):
    return HttpResponse("Agregar calificación - Vista temporal") 