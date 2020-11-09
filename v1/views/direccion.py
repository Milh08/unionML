from rest_framework import generics

from ..models.direccion import Direccion
from ..serializers.direccion import DireccionSerializer


class DireccionList(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class DireccionDetails(generics.RetrieveDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
