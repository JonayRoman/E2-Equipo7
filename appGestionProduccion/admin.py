from django.contrib import admin
from appGestionProduccion.models import Empleado, Proceso, Equipo, Orden_De_fabricacion
#Crear el modo admin de los cuatro modelos para poder administrarlos desde el "superuser"
admin.site.register(Empleado)
admin.site.register(Proceso)
admin.site.register(Equipo)
admin.site.register(Orden_De_fabricacion)