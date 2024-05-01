from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, DetailView

from appGestionProduccion.forms import EmpleadoForm, ProcesoForm, EquipoForm, OrdenForm
from appGestionProduccion.models import Empleado, Proceso, Equipo, Orden_De_fabricacion


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
    
#Lista de todos los procesos
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

#Ver el detalle de un proceso
def show_Proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    empleados = proceso.empleados_asignados.all()
    return render(request, 'appGestionProduccion/proceso_detail.html', {'proceso':proceso, 'empleados':empleados})

#Ver el detalle de un proceso
class ProcesoDetailView(DetailView):
    model = Proceso

def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    output = (f'Detalles del empleado: {empleado.id}, {empleado.nombre},'
              f' Empleados :{[e.nombre for e in empleado.proceso_set.all()]}')
    return HttpResponse(output)

#Listado de equipos
class EquipoListView(ListView):
    model = Equipo
    template_name = "appGestionProduccion/equipo_list.html"
    context_object_name = "equipos"

#Crear un nuevo equipo
class EquipoCreateView(View):
    def get(self, request):
        formulario = EquipoForm()
        context = {'formulario': formulario}
        return render(request, 'appGestionProduccion/equipo_create.html', context)

    def post(self, request):
        formulario = EquipoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('equipo_list')
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
        formulario = EquipoForm( instance=equipo)
        context = {
            'formulario': formulario,
            'empleado': equipo
        }
        return render(request, 'appGestionProduccion/equipo_update.html', context)
    # Llamada para procesar la actualización del equipo
    def post(self, request, pk):
        equipo = Equipo.objects.get(id= pk)
        formulario = EquipoForm(request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            return redirect('equipo_list')
        else:
            formulario = EquipoForm(instance=equipo)
        return render(request, 'appGestionProduccion/equipo_update.html', {'formulario': formulario})

#vista detallada del equipo
def show_Equipo(request, equipo_id):
    equipo = get_object_or_404(Proceso, id=equipo_id)
    return render(request, 'appGestionProduccion/equipo_detail.html', {'equipo':equipo})

class EquipoDetailView(DetailView):
    model = Equipo

#Lista de todas las ordenes (se ven todos los atributos)
class OrdenListView(ListView):
    model = Orden_De_fabricacion
    template_name = "appGestionProduccion/orden_list.html"
    context_object_name = "ordenes"

#DetailView de Ordenes de Fabricacion
class OrdenDetailView(DetailView):
    model = Orden_De_fabricacion


#Crear nueva Orden de Fabricacion
class OrdenCreateView(View):
    def get(self, request):
        formulario = OrdenForm()  # Utiliza el formulario correspondiente
        context = {'formulario': formulario}
        return render(request, 'appGestionProduccion/orden_create.html', context)

    def post(self, request):
        formulario = OrdenForm(data=request.POST)  # Utiliza el formulario correspondiente
        if formulario.is_valid():
            formulario.save()
            return redirect('orden_list')  # Redirige a la lista de órdenes
        return render(request, 'appGestionProduccion/orden_create.html', {'formulario': formulario})
    
#Modificar una orden de fabricacion
class OrdenUpdateView(View):
    def get(self, request, pk):
        orden = get_object_or_404(Orden_De_fabricacion, pk=pk)
        formulario = OrdenForm(instance=orden)
        context = {'formulario': formulario, 'orden': orden}
        return render(request, 'appGestionProduccion/orden_update.html', context)

    def post(self, request, pk):
        orden = get_object_or_404(Orden_De_fabricacion, pk=pk)
        formulario = OrdenForm(data=request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            return redirect('orden_detail', pk=pk)  # Redirige a la vista de detalle de la orden actualizada
        return render(request, 'appGestionProduccion/orden_update.html', {'formulario': formulario})
    
#Eliminar una orden de fabricacion
class OrdenDeleteView(DeleteView):
    model = Orden_De_fabricacion
    success_url = reverse_lazy('orden_list')
    