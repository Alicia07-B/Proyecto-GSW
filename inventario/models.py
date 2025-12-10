from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User

class Equipo(models.Model):
    numero_inventario = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio_adquisicion = models.DecimalField(max_digits=10, decimal_places=2)
    usuario_responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # Campos nuevos
    nombre = models.CharField(max_length=200, default="Equipo sin nombre")
    estado = models.CharField(max_length=20, default="activo")
    ubicacion = models.CharField(max_length=200, default="No especificada")
    fecha_adquisicion = models.DateField(null=True, blank=True)
    
    # Campo creado_en como nullable primero
    creado_en = models.DateTimeField(auto_now_add=True) # Primero nullable
    actualizado_en = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.numero_inventario} - {self.nombre}"
    
    def save(self, *args, **kwargs):
        if not self.creado_en:
            self.creado_en = timezone.now()
        super().save(*args, **kwargs)

        