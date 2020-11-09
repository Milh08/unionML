from django.db import models

from .mixins import TimestampMixin


class Modalidad(TimestampMixin):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
