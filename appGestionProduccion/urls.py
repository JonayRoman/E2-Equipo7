"""
URL configuration for proyectoEquipo7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoDeleteView, EmpleadoUpdateView, ProcesoListView, \
    ProcesoCreateView, ProcesoDeleteView, ProcesoUpdateView, ProcesoDetailView, EquipoListView, EquipoCreateView, \
    EquipoDeleteView, EquipoUpdateView, EquipoDetailView, OrdenListView, OrdenCreateView, \
    OrdenUpdateView, OrdenDeleteView

urlpatterns = [
    #Urls de los empleados
    path('/empleados', EmpleadoListView.as_view(), name='empleado_list'), #url listar empleados
    path('/empleados/create', EmpleadoCreateView.as_view(), name='empleado_create'), #url crear empleados
    path('/empleados/delete/<int:pk>', EmpleadoDeleteView.as_view(), name='empleados_delete'), #url borrar empleados
    path('/empleados/update/<int:pk>', EmpleadoUpdateView.as_view(), name='empleados_update'), #url modificar empleados
    #Urls de los procesos
    path('/procesos', ProcesoListView.as_view(), name='proceso_list'), #url listar procesos
    path('/proceso/create', ProcesoCreateView.as_view(), name='proceso_create'), #url crear procesos
    path('/proceos/delete/<int:pk>', ProcesoDeleteView.as_view(), name='proceso_delete'), #url borrar procesos
    path('/proceso/update/<int:pk>', ProcesoUpdateView.as_view(), name='proceso_update'), #url modificar procesos
    path('/proceso/<int:pk>', ProcesoDetailView.as_view(), name='procesos_show'), #url vista detallada procesos
    #Urls de los equipos
    path('/equipos', EquipoListView.as_view(), name='equipo_list'), #url listar equipos
    path('/equipos/create', EquipoCreateView.as_view(), name='equipo_create'), #url crear equipos
    path('/equipos/delete/<int:pk>', EquipoDeleteView.as_view(), name='equipos_delete'), #url borrar equipos
    path('/equipos/update/<int:pk>', EquipoUpdateView.as_view(), name='equipos_update'), #url modificar equipos
    path('/equipo/<int:pk>', EquipoDetailView.as_view(), name='equipo_show'), #url vista detallada equipos
    #Urls de las órdenes
    path('/ordenes', OrdenListView.as_view(), name='orden_list'), #url listar ordenes
    path('ordenes/create/', OrdenCreateView.as_view(), name='orden_create'), #url crear ordenes de fabricacion
    path('/ordenes/update/<int:pk>', OrdenUpdateView.as_view(), name='orden_update'), #url modificar ordenes de fabricacion
    path('ordenes/delete/<int:pk>/', OrdenDeleteView.as_view(), name='orden_delete'), #url borrar ordenes de fabricacion
]

