from django.db import models

from .mixins import TimestampMixin


class Lengua(TimestampMixin):
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    familia = models.CharField(max_length=255)
    agrupacion = models.CharField(max_length=255)
    originaria = models.BooleanField()
    extranjera = models.BooleanField()
    materia = models.BooleanField()

    def __str__(self):
        return self.nombre


TIPOS = [
    (1, 'Origen'),
    (2, 'Cursada'),
]


class PersonaLengua(TimestampMixin):
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    lengua = models.ForeignKey(Lengua, on_delete=models.CASCADE)
    read = models.PositiveSmallIntegerField()
    listening = models.PositiveSmallIntegerField()
    written = models.PositiveSmallIntegerField()
    speaking = models.PositiveSmallIntegerField()
    tipo = models.PositiveSmallIntegerField(choices=TIPOS)
    comentarios = models.CharField(max_length=200, blank=True)
