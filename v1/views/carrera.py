from rest_framework import generics

from ..models.carrera import Carrera
from ..serializers.carrera import (CarreraListSerializer,
                                   CarreraCreateSerializer,
                                   CarreraRetrieveSerializer)


class CarreraList(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarreraListSerializer
        return CarreraCreateSerializer


class CarreraDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrera.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarreraRetrieveSerializer
        return CarreraCreateSerializer
