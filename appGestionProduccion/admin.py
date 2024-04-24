from django.contrib import admin
from appGestionProduccion.models import Empleado, Proceso, Equipo, Orden_De_fabricacion

admin.site.register(Empleado)
admin.site.register(Proceso)
admin.site.register(Equipo)
admin.site.register(Orden_De_fabricacion)