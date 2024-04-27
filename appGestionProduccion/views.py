from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView

from appGestionProduccion.forms import EmpleadoForm, ProcesoForm
from appGestionProduccion.models import Empleado, Proceso

#Lista de todos los empleados (se ven todos los atributos)
class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appGestionProduccion/empleado_list.html"
    context_object_name = "empleados"

#Crear un nuevo empleado
class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        return render(request, 'appGestionProduccion/empleado_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_list')
        return render(request, 'appGestionProduccion/empleado_create.html', {'formulario': formulario})

#Eliminar un empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleado_list')

#Modificar un empleado
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    def get(self, request, pk):
        empleado = Empleado.objects.get(id=pk)
        formulario = EmpleadoForm( instance=empleado)
        context = {
            'formulario': formulario,
            'empleado': empleado
        }
        return render(request, 'appGestionProduccion/empleado_update.html', context)
    # Llamada para procesar la actualización del empleado
    def post(self, request, pk):
        empleado = Empleado.objects.get(id= pk)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_list')
        else:
            formulario = EmpleadoForm(instance=empleado)
        return render(request, 'appGestionProduccion/empleado_update.html', {'formulario': formulario})
    
#Lista de todos los procesos (se ven todos los atributos)    
class ProcesoListView(ListView):
    model = Proceso
    template_name = "appGestionProduccion/proceso_list.html"
    context_object_name = "procesos"
    
#Crear un nuevo proceso
class ProcesoCreateView(View):
    def get(self, request):
        formulario = ProcesoForm()
        context = {'formulario': formulario}
        return render(request, 'appGestionProduccion/proceso_create.html', context)

    def post(self, request):
        formulario = ProcesoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('proceso_list')
        return render(request, 'appGestionProduccion/proceso_create.html', {'formulario': formulario})

#Eliminar un proceso
class ProcesoDeleteView(DeleteView):
    model = Proceso
    success_url = reverse_lazy('proceso_list')

#Modificar un proceso
class ProcesoUpdateView(UpdateView):
    model = Proceso
    def get(self, request, pk):
        proceso = Proceso.objects.get(id=pk)
        formulario = ProcesoForm( instance=proceso)
        context = {
            'formulario': formulario,
            'proceso': proceso
        }
        return render(request, 'appGestionProduccion/proceso_update.html', context)
    # Llamada para procesar la actualización del proceso
    def post(self, request, pk):
        proceso = Proceso.objects.get(id= pk)
        formulario = ProcesoForm(request.POST, instance=proceso)
        if formulario.is_valid():
            formulario.save()
            return redirect('proceso_list')
        else:
            formulario = ProcesoForm(instance=proceso)
        return render(request, 'appGestionProduccion/proceso_update.html', {'formulario': formulario})