from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from appGestionProduccion.forms import EmpleadoForm
from appGestionProduccion.models import Empleado

#Lista de todos los empleados (se ven todos los atributos)
class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appGestionProduccion/empleado_list.html"
    context_object_name = "empleados"


class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        return render(request, 'appGestionProduccion/empleado_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        return render(request, 'appGestionProduccion/empleado_create.html', {'formulario': formulario})