from django.urls import path # type: ignore
from . import views

app_name = 'calificaciones'

urlpatterns = [
    path('', views.listar_calificaciones, name='listar_calificaciones'),
    # Cambia esta línea:
    path('agregar/', views.agregar_calificacion, name='agregar_calificacion'),
]