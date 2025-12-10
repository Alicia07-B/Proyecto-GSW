from django.shortcuts import render
from django.http import HttpResponse # type: ignore

def listar_equipos(request):
    equipos = []  # Lista vacía por ahora
    return render(request, 'inventario/listar_equipos.html', {'equipos': equipos})

# ¡AGREGA ESTA FUNCIÓN!
def crear_equipo(request):
    return HttpResponse("Página para crear equipo - funciona")

def agregar_equipo(request):
    return crear_equipo(request)  # Redirige a crear_equipo

def detalle_equipo(request, equipo_id):
    return HttpResponse(f"Detalle equipo {equipo_id}") 