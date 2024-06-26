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

#Clase para los formularios del modelo Proceso para que no tenga en cuenta el archivo en la vista de modificacion
class ProcesoUpdateForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['codigo_proceso', 'nombre_proceso', 'referencia', 'equipo', 'fecha_inicio', 'fecha_fin', 'referencia_de_fabricacion', 'empleados_asignados']

#Clase para los formularios del modelo Equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

#Clase para los formularios del modelo Equipo para que no tenga en cuenta el archivo en la vista de modificacion
class EquipoUpdateForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['modelo', 'marca', 'tipo', 'fecha_adquisicion', 'fecha_instalacion']

#Clase para los formularios del modelo orden_De_fabricacion
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden_De_fabricacion
        fields = '__all__'