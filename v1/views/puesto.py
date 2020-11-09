from rest_framework import generics

# ---- Models ----
from ..models.puesto import Puesto, PuestoEmpleado

# ---- Serializer ----
from ..serializers.puesto import PuestoSerializer, PuestoEmpleadoSerializer


class PuestoList(generics.ListCreateAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer


class PuestoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer


class PuestoEmpleadoList(generics.ListCreateAPIView):
    queryset = PuestoEmpleado.objects.all()
    serializer_class = PuestoEmpleadoSerializer


class PuestoEmpleadoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuestoEmpleado.objects.all()
    serializer_class = PuestoEmpleadoSerializer