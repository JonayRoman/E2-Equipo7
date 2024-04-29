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
from . import views
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoDeleteView, EmpleadoUpdateView, ProcesoListView, \
    ProcesoCreateView, ProcesoDeleteView, ProcesoUpdateView, ProcesoDetailView, EquipoListView, EquipoCreateView, \
    EquipoDeleteView, EquipoUpdateView, EquipoDetailView

urlpatterns = [
    path('/empleados', EmpleadoListView.as_view(), name='empleado_list'),
    path('/empleados/create', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('/empleados/delete/<int:pk>', EmpleadoDeleteView.as_view(), name='empleados_delete'),
    path('/empleados/update/<int:pk>', EmpleadoUpdateView.as_view(), name='empleados_update'),
    path('/procesos', ProcesoListView.as_view(), name='proceso_list'),
    path('/proceso/create', ProcesoCreateView.as_view(), name='proceso_create'),
    path('/proceos/delete/<int:pk>', ProcesoDeleteView.as_view(), name='proceso_delete'),
    path('/proeso/update/<int:pk>', ProcesoUpdateView.as_view(), name='proceso_update'),
    path('/proceso/<int:pk>', ProcesoDetailView.as_view(), name='procesos_show'),
    path('/procesos/<int:empleado_id>', views.show_empleado, name="empleados_show"), #esta mal
    path('/equipos', EquipoListView.as_view(), name='equipo_list'),
    path('/equipos/create', EquipoCreateView.as_view(), name='equipo_create'),
    path('/equipos/delete/<int:pk>', EquipoDeleteView.as_view(), name='equipos_delete'),
    path('/equipos/update/<int:pk>', EquipoUpdateView.as_view(), name='equipos_update'),
    path('/equipo/<int:pk>', EquipoDetailView.as_view(), name='equipo_show'),
]
