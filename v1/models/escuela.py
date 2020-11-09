from django.db import models

from .mixins import TimestampMixin


class Escuela(TimestampMixin):
    cct = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    acronimo = models.CharField(max_length=255, blank=True)
    plantel = models.PositiveSmallIntegerField(null=True)
    is_num = models.BooleanField(default=False)
    nivel = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=255)
    grado = models.CharField(max_length=255, blank=True)
    sector = models.BooleanField(default=True)
    municipio = models.CharField(max_length=255)
    entidad = models.CharField(max_length=255, default='CHIAPAS', blank=True)
    pais = models.CharField(max_length=255, default='MÉXICO', blank=True)
