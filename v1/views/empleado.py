from rest_framework import generics


# -------- Models --------
from ..models.empleado import Empleado
from ..models.direccion import Direccion
from ..models.categorias import CategoriaEmpleado

# -------- Serializers --------
from ..serializers.empleado import (EmpleadoCreateSerializer,
                                    EmpleadoUpdateSerializer,
                                    EmpleadoListSerializer,
                                    EmpleadoDetailSerializer)


class EmpleadoList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmpleadoCreateSerializer
        return EmpleadoListSerializer


class EmpleadoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return EmpleadoUpdateSerializer
        return EmpleadoDetailSerializer

    def perform_destroy(self, instance):
        direcciones = Direccion.objects.filter(persona=instance)
        direcciones.delete()

        categorias = CategoriaEmpleado.objects.filter(empleado=instance)
        categorias.delete()

        instance.delete()