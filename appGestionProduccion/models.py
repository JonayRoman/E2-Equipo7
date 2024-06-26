from django.db import models

#Modelo para la clase Empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"
    class Meta:
        verbose_name_plural = "Empleados"
        verbose_name = "Empleado"
        ordering = ["-created"]

#Modelo para la clase Orden de fabricacion
class Orden_De_fabricacion(models.Model):
    ref_fabricacion = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.ref_fabricacion})"
    class Meta:
        verbose_name_plural = "Ordenes de fabricacion"
        verbose_name = "Orden de fabricacion"
        ordering = ["-created"]

#Modelo para la clase Equipo
class Equipo(models.Model):
    modelo = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()
    archivo = models.FileField(upload_to='equipo/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.modelo} ({self.tipo})"
    class Meta:
        verbose_name_plural = "Equipos"
        verbose_name = "Equipo"
        ordering = ["-created"]

#Modelo para la clase Proceso
class Proceso(models.Model):
    codigo_proceso = models.CharField(max_length=10, unique=True)
    nombre_proceso = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    referencia_de_fabricacion = models.ManyToManyField(Orden_De_fabricacion)
    empleados_asignados = models.ManyToManyField(Empleado)
    archivo = models.FileField(upload_to='procesos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_proceso} ({self.codigo_proceso})"
    class Meta:
        verbose_name_plural = "Procesos"
        verbose_name = "Proceso"
        ordering = ["-created"]
