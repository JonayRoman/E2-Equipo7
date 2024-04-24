from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from appGestionProduccion.models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appGestionProduccion/empleado_list.html"
    context_object_name = "empleados"