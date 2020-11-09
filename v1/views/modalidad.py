from rest_framework import generics

from ..models.modalidad import Modalidad
from ..serializers.modalidad import ModalidadSerializer


class ModalidadList(generics.ListCreateAPIView):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer


class ModalidadDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer
