from django.urls import path # type: ignore
from . import views

app_name = 'accesibilidad'  # Agregar esta línea para definir el espacio de nombres

urlpatterns = [
    path('', views.index, name='index'),
    path('recursos/', views.listar_recursos, name='listar_recursos'),
    path('recursos/<int:recurso_id>/', views.detalle_recurso, name='detalle_recurso'),
    path('mis-solicitudes/', views.mis_solicitudes, name='mis_solicitudes'),
]
