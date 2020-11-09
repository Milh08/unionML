from rest_framework import serializers

from ..models.categorias import Categoria, CategoriaAlumno, CategoriaEmpleado


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'clave', 'nombre']


class CategoriaAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAlumno
        fields = ['id', 'clave', 'nombre']


class CategoriaEmpleadoSerializer(serializers.ModelSerializer):
    """ Serializer para relación Categoria-Empleado """
    id_categoria = serializers.ReadOnlyField(source='categoria.id')
    nombre = serializers.ReadOnlyField(source='categoria.nombre')
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
        write_only=True,
    )

    class Meta:
        model  = CategoriaEmpleado
        fields = [
            'id', 'id_categoria', 'nombre', 'categoria_id', 
            'promocion', 'comentarios'
        ]
    

class CategoriaEmpleadoReducedSerializer(serializers.ModelSerializer):
    """ Serializer para relación Categoria-Empleado """
    id = serializers.ReadOnlyField(source='categoria.id')
    nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model  = CategoriaEmpleado
        fields = ['id', 'nombre',]