from django.db import models # type: ignore
from django.contrib.auth.models import User

class RecursoAccesibilidad(models.Model):
    TIPO_CHOICES = [
        ('visual', 'Visual'),
        ('auditivo', 'Auditivo'),
        ('motor', 'Motor'),
        ('cognitivo', 'Cognitivo'),
    ]
    
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('mantenimiento', 'En Mantenimiento'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ubicacion = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_adquisicion = models.DateField()
    ultimo_mantenimiento = models.DateField(null=True, blank=True)
    proximo_mantenimiento = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Recurso de Accesibilidad'
        verbose_name_plural = 'Recursos de Accesibilidad'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_display()}"
    
    def necesita_mantenimiento(self):
        if self.proximo_mantenimiento:
            from datetime import date
            return date.today() >= self.proximo_mantenimiento
        return False


class SolicitudAcceso(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('completada', 'Completada'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recurso = models.ForeignKey(RecursoAccesibilidad, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Solicitud de Acceso'
        verbose_name_plural = 'Solicitudes de Acceso'
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"Solicitud {self.id} - {self.usuario.username}"