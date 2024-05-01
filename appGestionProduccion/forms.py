from django import forms

from appGestionProduccion.models import Empleado, Proceso, Equipo, Orden_De_fabricacion

#Clase para los formularios del modelo Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

#Clase para los formularios del modelo Proceso
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = '__all__'

#Clase para los formularios del modelo Equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

#Clase para los formularios del modelo orden_De_fabricacion
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden_De_fabricacion
        fields = '__all__'