from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['numero_inventario', 'descripcion', 'precio_adquisicion', 'usuario_responsable']
        