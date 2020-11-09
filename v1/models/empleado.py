from django.db import models

from .persona import Persona

class Empleado(Persona):
    persona         = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        parent_link=True
    )
    docente         = models.IntegerField(default=0)
    grado_nivel     = models.CharField(max_length=30, blank=True)
    grado_academico = models.CharField(max_length=50, blank=True)
    grado_estatus   = models.CharField(max_length=20, blank=True)
    grado_firma     = models.CharField(max_length=10, blank=True)