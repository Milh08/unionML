from rest_framework import generics

from ..models.alumno import Alumno
from ..models.direccion import Direccion
from ..models.lengua import PersonaLengua
from ..serializers.alumno import (AlumnoListSerializer,
                                  AlumnoCreateSerializer,
                                  AlumnoUpdateSerializer)


class AlumnoList(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AlumnoCreateSerializer
        return AlumnoListSerializer


class AlumnoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return AlumnoUpdateSerializer
        return AlumnoListSerializer

    def perform_destroy(self, instance):
        direcciones = Direccion.objects.filter(persona=instance)
        direcciones.delete()

        lenguas = PersonaLengua.objects.filter(persona=instance)
        lenguas.delete()

        instance.delete()
