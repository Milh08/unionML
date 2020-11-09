from rest_framework import generics

# -------- Models --------
from ..models.categorias import Categoria, CategoriaAlumno, CategoriaEmpleado

# -------- Serializers --------
from ..serializers.categorias import (CategoriaSerializer,
                                      CategoriaAlumnoSerializer,
                                      CategoriaEmpleadoSerializer)


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaAlumnoList(generics.ListCreateAPIView):
    queryset = CategoriaAlumno.objects.all()
    serializer_class = CategoriaAlumnoSerializer


class CategoriaAlumnoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaAlumno.objects.all()
    serializer_class = CategoriaAlumnoSerializer


class CategoriaEmpleadoList(generics.ListCreateAPIView):
    queryset = CategoriaEmpleado.objects.all()
    serializer_class = CategoriaEmpleadoSerializer


class CategoriaEmpleadoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaEmpleado.objects.all()
    serializer_class = CategoriaEmpleadoSerializer