import datetime

from django.db import models

from .mixins import TimestampMixin
from .modalidad import Modalidad
from .division import Division


class Carrera(TimestampMixin):
    clave = models.CharField(max_length=5)
    clave_dgp = models.CharField(max_length=6)
    clave_ceneval = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=30)
    periodicidad = models.CharField(max_length=30, default='SEMESTRAL', blank=True)
    vigencia = models.DateField()
    modalidad = models.ForeignKey(
        Modalidad,
        on_delete=models.CASCADE,
        related_name='carreras',
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='carreras',
    )
