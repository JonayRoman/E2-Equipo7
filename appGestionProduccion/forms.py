from django import forms

from appGestionProduccion.models import Empleado, Proceso, Equipo


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = '__all__'

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'