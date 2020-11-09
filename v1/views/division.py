from rest_framework import generics

# ---- Models ----
from ..models.division import Division

# ---- Serializer ----
from ..serializers.division import (DivisionCreateSerializer,
                                    DivisionListSerializer)


class DivisionList(generics.ListCreateAPIView):
    queryset = Division.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DivisionListSerializer
        return DivisionCreateSerializer


class DivisionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Division.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DivisionListSerializer
        return DivisionCreateSerializer