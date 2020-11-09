from django.db import models

from .persona import Persona
from .mixins import TimestampMixin


TIPOS = [
    (1, 'Origen'),
    (2, 'Actual'),
    (3, 'Egresado'),
]


class Direccion(TimestampMixin):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='direcciones'
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS, default=1)
    codigo_postal = models.CharField(max_length=5)
    pais = models.CharField(max_length=50)
    entidad = models.CharField(max_length=50)
    municipio = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    calle = models.CharField(max_length=200)
