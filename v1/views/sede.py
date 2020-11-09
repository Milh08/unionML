from rest_framework import generics

from ..models.sede import Sede
from ..serializers.sede import (SedeListSerializer,
                                SedeCreateSerializer,
                                SedeRetrieveSerializer)


class SedeList(generics.ListCreateAPIView):
    queryset = Sede.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SedeCreateSerializer
        return SedeListSerializer


class SedeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sede.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return SedeCreateSerializer
        return SedeRetrieveSerializer
