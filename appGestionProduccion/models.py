from django.db import models

class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"
    class Meta:
        verbose_name_plural = "Empleados"
        verbose_name = "Empleado"
        ordering = ["-created"]

class Proceso(models.Model):
    codigo_orden_fabricacion = models.CharField(max_length=10) #foreign key de orden de fav
    codigo_proceso = models.CharField(max_length=10, unique=True)
    nombre_proceso = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50) #foreign key de equipo
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    empleado_asignados = models.ManyToManyField(Empleado) #foreign key de empleado
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_proceso} ({self.codigo_proceso})"
    class Meta:
        verbose_name_plural = "Procesos"
        verbose_name = "Proceso"
        ordering = ["-created"]

class Equipo(models.Model):
    modelo = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.modelo} ({self.tipo})"
    class Meta:
        verbose_name_plural = "Equipos"
        verbose_name = "Equipo"
        ordering = ["-created"]

class orden_De_fabricacion(models.Model):
    ref_fabricacion = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.ref_fabricacion})"
    class Meta:
        verbose_name_plural = "Ordenes de fabricacion"
        verbose_name = "Orden de fabricacion"
        ordering = ["-created"]
