from rest_framework import generics

from ..models.lengua import Lengua
from ..serializers.lengua import LenguaSerializer


class LenguaList(generics.ListCreateAPIView):
    queryset = Lengua.objects.all()
    serializer_class = LenguaSerializer


class LenguaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lengua.objects.all()
    serializer_class = LenguaSerializer
