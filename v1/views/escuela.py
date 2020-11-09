from rest_framework import generics

from ..models.escuela import Escuela
from ..serializers.escuela import EscuelaSerializer


class EscuelaList(generics.ListCreateAPIView):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer


class EscuelaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer
