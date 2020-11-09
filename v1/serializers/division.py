from rest_framework import serializers

from ..models.division import Division, DivisionEmpleado


class DivisionListSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar datos de las Divisiones. """
    tipo = serializers.SerializerMethodField()

    class Meta:
        model = Division
        fields = ['id', 'nombre', 'tipo']

    def get_tipo(self, obj):
        if obj.is_depto:
            return "Departamento"
        return "División"


class DivisionCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar una División. """
    class Meta:
        model = Division
        fields = [
            'id', 'nombre', 'is_depto', 'parent', 'superior_at',
        ]


class DivisionEmpleadoSerializer(serializers.ModelSerializer):
    """ Serializer para la relacion Division-Empleado """
    id_division = serializers.ReadOnlyField(source='division.id')
    nombre = serializers.ReadOnlyField(source='division.nombre')
    division_id = serializers.PrimaryKeyRelatedField(
        queryset = Division.objects.all(),
        source = 'division',
        write_only = True,
    )

    class Meta:
        model = DivisionEmpleado
        fields = [
            'id', 'id_division', 'nombre', 'division_id',
            'promocion', 'comentarios'
        ]


class DivisionEmpleadoReducedSerializer(serializers.ModelSerializer):
    """ Serializer para la relacion Division-Empleado """
    id = serializers.ReadOnlyField(source='division.id')
    nombre = serializers.ReadOnlyField(source='division.nombre')

    class Meta:
        model = DivisionEmpleado
        fields = ['id', 'nombre',]