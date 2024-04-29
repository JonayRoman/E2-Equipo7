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
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoDeleteView, EmpleadoUpdateView, ProcesoListView, ProcesoCreateView, ProcesoDeleteView, ProcesoUpdateView

urlpatterns = [
    path('/empleados', EmpleadoListView.as_view(), name='empleado_list'),
    path('/empleados/create', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('/empleados/delete/<int:pk>', EmpleadoDeleteView.as_view(), name='empleados_delete'),
    path('/empleados/update/<int:pk>', EmpleadoUpdateView.as_view(), name='empleados_update'),
    path('/procesos', ProcesoListView.as_view(), name='proceso_list'),
    path('/proceso/create', ProcesoCreateView.as_view(), name='proceso_create'),
    path('/proceos/delete/<int:pk>', ProcesoDeleteView.as_view(), name='proceso_delete'),
    path('/proeso/update/<int:pk>', ProcesoUpdateView.as_view(), name='proceso_update'),
]
