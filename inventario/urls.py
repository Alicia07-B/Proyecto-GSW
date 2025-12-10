from django.urls import path # type: ignore
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.listar_equipos, name='listar_equipos'),
    path('crear/', views.crear_equipo, name='crear_equipo'),  # ¡IMPORTANTE!
    path('agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
]