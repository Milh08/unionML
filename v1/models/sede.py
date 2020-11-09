import datetime

from django.db import models

from .mixins import TimestampMixin
from .empleado import Empleado


class Sede(TimestampMixin):
    clave = models.CharField(max_length=5)
    clave_ceneval = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    entidad = models.CharField(max_length=30, blank=True, default='CHIAPAS')
    pais = models.CharField(max_length=30, blank=True, default='MÉXICO')
    codigo_postal = models.CharField(max_length=5)
    portal_web = models.CharField(max_length=100, blank=True)
    correo_electronico = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    extension = models.CharField(max_length=20, blank=True)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True)

    def __str__(self):
        return self.nombre


class SedeEmpleado(TimestampMixin):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    promocion = models.DateField(null=True)
    comentarios = models.TextField(null=True)