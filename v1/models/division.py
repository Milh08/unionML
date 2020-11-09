from django.db import models

from .mixins import TimestampMixin
from .empleado import Empleado


class Division(TimestampMixin):
    nombre = models.CharField(max_length=50)
    is_depto = models.BooleanField(default=True)
    parent = models.PositiveIntegerField(null=True)
    superior_at = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.nombre


class DivisionEmpleado(TimestampMixin):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    promocion   = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)