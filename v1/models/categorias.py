from django.db import models

from .mixins import TimestampMixin
from .empleado import Empleado

class Categoria(TimestampMixin):
    clave  = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=30)

# -------- Alumno --------
class CategoriaAlumno(TimestampMixin):
    clave = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.clave, self.nombre)

# -------- Empleado --------
class CategoriaEmpleado(TimestampMixin):
    empleado    = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    promocion   = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)