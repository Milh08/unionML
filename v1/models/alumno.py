from django.db import models

from .persona import Persona
from .categorias import CategoriaAlumno


class Alumno(Persona):
    persona = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        parent_link=True
    )
    categoria = models.ForeignKey(
        CategoriaAlumno,
        on_delete=models.CASCADE
    )
    graduado = models.BooleanField(default=False)
    graduado_fecha = models.DateField(null=True)
    old_matricula = models.CharField(max_length=10)
