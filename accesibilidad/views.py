from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import RecursoAccesibilidad

def index(request):
    """Vista principal de accesibilidad"""
    messages.success(request, 'Bienvenido al sistema de accesibilidad')
    
    recursos = RecursoAccesibilidad.objects.all()[:5]
    
    context = {
        'recursos': recursos,
        'titulo': 'Sistema de Accesibilidad',
    }
    return render(request, 'accesibilidad/index.html', context)

def listar_recursos(request):
    """Listar todos los recursos"""
    recursos = RecursoAccesibilidad.objects.all()
    context = {
        'recursos': recursos,
        'titulo': 'Todos los Recursos',
    }
    return render(request, 'accesibilidad/listar_recursos.html', context)

def mis_solicitudes(request):
    """Vista para mis solicitudes"""
    context = {
        'titulo': 'Mis Solicitudes',
    }
    return render(request, 'accesibilidad/mis_solicitudes.html', context)

def detalle_recurso(request, recurso_id):
    """Vista para mostrar los detalles de un recurso específico"""
    recurso = get_object_or_404(RecursoAccesibilidad, id=recurso_id)
    context = {
        'recurso': recurso,
        'titulo': recurso.nombre,  # Usar el nombre del recurso como título
    }
    return render(request, 'accesibilidad/detalle_recurso.html', context)
