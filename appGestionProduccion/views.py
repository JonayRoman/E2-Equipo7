from venv import logger

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
import logging
from .logging import logger as loggerCrearModificar

from appGestionProduccion.forms import EmpleadoForm, ProcesoForm, EquipoForm, OrdenForm, EquipoUpdateForm, \
    ProcesoUpdateForm
from appGestionProduccion.models import Empleado, Proceso, Equipo, Orden_De_fabricacion

#Lista de todos los empleados (se ven todos los atributos)
class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appGestionProduccion/empleado_list.html"
    context_object_name = "empleados"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Empleado.objects.filter(nombre__icontains=query)
        return Empleado.objects.all()

#Crear un nuevo empleado
class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        loggerCrearModificar.info('Has entrado a la pagina para crear un empleado')
        return render(request, 'appGestionProduccion/empleado_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        nombre = formulario.data.get('nombre', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('Nuevo empleado creado con el nombre "%s".', nombre)
            return redirect('empleado_list')
        else:
            loggerCrearModificar.warning('Error al crear el empleado: "%s".', nombre)
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
        loggerCrearModificar.info('Has entrado a la pagina para modificar "%s".', empleado.nombre)
        return render(request, 'appGestionProduccion/empleado_update.html', context)
    # Llamada para procesar la actualización del empleado
    def post(self, request, pk):
        empleado = Empleado.objects.get(id= pk)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        nombre = formulario.data.get('nombre', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('Modificacion exitosa del empleado "%s".', nombre)
            return redirect('empleado_list')
        else:
            formulario = EmpleadoForm(instance=empleado)
            loggerCrearModificar.warning('Error al intentar realizar la modificacion para "%s".', nombre)
        return render(request, 'appGestionProduccion/empleado_update.html', {'formulario': formulario})
    
#Lista de todos los procesos
class ProcesoListView(ListView):
    model = Proceso
    template_name = "appGestionProduccion/proceso_list.html"
    context_object_name = "procesos"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Proceso.objects.filter(nombre_proceso__icontains=query)
        return Proceso.objects.all()
    
#Crear un nuevo proceso
class ProcesoCreateView(View):
    def get(self, request):
        formulario = ProcesoForm()
        context = {'formulario': formulario}
        loggerCrearModificar.info('Has entrado a la pagina para crear un proceso')
        return render(request, 'appGestionProduccion/proceso_create.html', context)

    def post(self, request):
        formulario = ProcesoForm(data=request.POST, files=request.FILES)
        proceso_nombre = formulario.data.get('nombre_proceso', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('Nuevo proceso creado con el nombre "%s".', proceso_nombre)
            return redirect('proceso_list')
        else:
            loggerCrearModificar.warning('Error al crear el proceso: "%s".', proceso_nombre)
        return render(request, 'appGestionProduccion/proceso_create.html', {'formulario': formulario})

# Eliminar un proceso
class ProcesoDeleteView(DeleteView):
    model = Proceso
    success_url = reverse_lazy('proceso_list')

    def delete(self, request, *args, **kwargs):
        # Obtener el proceso que se va a eliminar
        proceso = self.get_object()

#Modificar un proceso
class ProcesoUpdateView(UpdateView):
    model = Proceso
    def get(self, request, pk):
        proceso = Proceso.objects.get(id=pk)
        formulario = ProcesoUpdateForm( instance=proceso)
        context = {
            'formulario': formulario,
            'proceso': proceso
        }
        loggerCrearModificar.info('Has entrado a la pagina para modificar "%s".', proceso.nombre_proceso)
        return render(request, 'appGestionProduccion/proceso_update.html', context)
    # Llamada para procesar la actualización del proceso
    def post(self, request, pk):
        proceso = Proceso.objects.get(id= pk)
        formulario = ProcesoUpdateForm(request.POST, instance=proceso)
        proceso_nombre = formulario.data.get('nombre_proceso', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('modificado con exito el proceso "%s".', proceso_nombre)
            return redirect('proceso_list')
        else:
            formulario = ProcesoForm(instance=proceso)
            loggerCrearModificar.warning('Error al intentar realizar la modificacion del proceso "%s".', proceso_nombre)
        return render(request, 'appGestionProduccion/proceso_update.html', {'formulario': formulario})

#Ver el detalle de un proceso
def show_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    equipo = proceso.equipos_asignados.all()

    return render(request, 'appGestionProduccion/proceso_detail.html', {'proceso':proceso, 'equipos':equipo})

#Ver el detalle de un proceso
class ProcesoDetailView(DetailView):
    model = Proceso

#Listado de equipos
class EquipoListView(ListView):
    model = Equipo
    template_name = "appGestionProduccion/equipo_list.html"
    context_object_name = "equipos"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Equipo.objects.filter(modelo__icontains=query)
        return Equipo.objects.all()

#Crear un nuevo equipo
class EquipoCreateView(View):
    def get(self, request):
        formulario = EquipoForm()
        context = {'formulario': formulario}
        loggerCrearModificar.info('Has entrado a la pagina para crear un equipo')
        return render(request, 'appGestionProduccion/equipo_create.html', context)

    def post(self, request):
        formulario = EquipoForm(data=request.POST, files=request.FILES)
        equipo_modelo = formulario.data.get('modelo', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('Nuevo equipo creado cuyo modelo es "%s".', equipo_modelo)
            return redirect('equipo_list')
        else:
            loggerCrearModificar.warning('Error al crear el equipo con modelo: "%s".', equipo_modelo)
        return render(request, 'appGestionProduccion/equipo_create.html', {'formulario': formulario})

#Eliminar un equipo
class EquipoDeleteView(DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipo_list')

#Modificar un equipo
class EquipoUpdateView(UpdateView):
    model = Equipo
    def get(self, request, pk):
        equipo = Equipo.objects.get(id=pk)
        formulario = EquipoUpdateForm( instance=equipo)
        context = {
            'formulario': formulario,
            'empleado': equipo
        }
        loggerCrearModificar.info('Has entrado a la pagina para modificar el equipo con modelo "%s".', equipo.modelo)
        return render(request, 'appGestionProduccion/equipo_update.html', context)
    # Llamada para procesar la actualización del equipo
    def post(self, request, pk):
        equipo = Equipo.objects.get(id= pk)
        formulario = EquipoUpdateForm(request.POST, instance=equipo)
        equipo_modelo = formulario.data.get('modelo', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('modificado con exito el modelo "%s".', equipo_modelo)
            return redirect('equipo_list')
        else:
            formulario = EquipoForm(instance=equipo)
            loggerCrearModificar.warning('Error al intentar realizar la modificacion del modelo "%s".', equipo_modelo)
        return render(request, 'appGestionProduccion/equipo_update.html', {'formulario': formulario})

#vista detallada del equipo
def show_Equipo(request, equipo_id):
    equipo = get_object_or_404(Proceso, id=equipo_id)
    return render(request, 'appGestionProduccion/equipo_detail.html', {'equipo':equipo})

#Vista detallada del equipo utilizado en procesos
class EquipoDetailView(DetailView):
    model = Equipo
    success_url = reverse_lazy('index')

#Lista de todas las ordenes (se ven todos los atributos)
class OrdenListView(ListView):
    model = Orden_De_fabricacion
    template_name = "appGestionProduccion/orden_list.html"
    context_object_name = "ordenes"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Orden_De_fabricacion.objects.filter(nombre__icontains=query)
        return Orden_De_fabricacion.objects.all()

#Crear nueva Orden de Fabricacion
class OrdenCreateView(View):
    def get(self, request):
        formulario = OrdenForm()
        context = {'formulario': formulario}
        loggerCrearModificar.info('Has entrado a la pagina para crear una orden')
        return render(request, 'appGestionProduccion/orden_create.html', context)

    def post(self, request):
        formulario = OrdenForm(data=request.POST)
        orden_nombre = formulario.data.get('nombre', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('Nueva orden creada con nombre "%s".', orden_nombre)
            return redirect('orden_list')
        else:
            loggerCrearModificar.warning('Error al crear la orden "%s".', orden_nombre)
        return render(request, 'appGestionProduccion/orden_create.html', {'formulario': formulario})
    
#Modificar una orden de fabricacion
class OrdenUpdateView(UpdateView):
    model = Orden_De_fabricacion
    def get(self, request, pk):
        orden = Orden_De_fabricacion.objects.get(id=pk)
        formulario = OrdenForm( instance=orden)
        orden_nombre = formulario.data.get('nombre', 'desconocido')
        context = {
            'formulario': formulario,
            'orden': orden
        }
        loggerCrearModificar.info('Has entrado a la pagina para modificar la orden "%s".', orden_nombre)
        return render(request, 'appGestionProduccion/orden_update.html', context)
    # Llamada para procesar la actualización de la orden de fabricacion
    def post(self, request, pk):
        orden = Orden_De_fabricacion.objects.get(id=pk)
        formulario = OrdenForm(request.POST, instance=orden)
        orden_nombre = formulario.data.get('nombre', 'desconocido')
        if formulario.is_valid():
            formulario.save()
            loggerCrearModificar.info('modificada con exito la orden "%s".', orden_nombre)
            return redirect('orden_list')
        else:
            formulario = OrdenForm(instance=orden)
            loggerCrearModificar.warning('Error al intentar realizar la modificacion de la orden "%s".', orden_nombre)
        return render(request, 'appGestionProduccion/orden_update.html', {'formulario': formulario})
    
#Eliminar una orden de fabricacion
class OrdenDeleteView(DeleteView):
    model = Orden_De_fabricacion
    success_url = reverse_lazy('orden_list')


    