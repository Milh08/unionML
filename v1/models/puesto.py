from django.db import models

from .mixins import TimestampMixin
from .empleado import Empleado


class Puesto(TimestampMixin):
    nombre = models.CharField(max_length=50)


class PuestoEmpleado(TimestampMixin):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    promocion = models.DateField(null=True)
    comentarios = models.TextField(null=True)