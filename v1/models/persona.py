import datetime

from django.db import models

from .lengua import Lengua, PersonaLengua
from .mixins import TimestampMixin


class Persona(TimestampMixin):
    curp = models.CharField(max_length=18)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    sexo = models.CharField(max_length=6)
    estado_civil = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=30, blank=True)
    nacionalidad = models.CharField(max_length=30)
    rfc = models.CharField(max_length=13)
    nss = models.CharField(max_length=11)
    correo_electronico = models.EmailField()
    telefono_casa = models.CharField(max_length=20)
    telefono_celular = models.CharField(max_length=20)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    folder_at = models.CharField(max_length=50, blank=True)
    status_at = models.BooleanField(default=True)
    lenguas = models.ManyToManyField(Lengua, through=PersonaLengua)

    def __str__(self):
        return '{} {} {}'.format(
            self.nombre,
            self.apellido_paterno,
            self.apellido_materno
        )

    @property
    def edad(self):
        today = datetime.date.today()
        return (today.year - self.fecha_nacimiento.year) - int(
            (today.month, today.day) <
            (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    @property
    def antiguedad(self):
        today = datetime.date.today()
        return (today.year - self.fecha_inicio.year) - int(
            (today.month, today.day) <
            (self.fecha_inicio.month, self.fecha_inicio.day))
