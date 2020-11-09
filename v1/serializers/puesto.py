from rest_framework import serializers

from ..models.puesto import Puesto, PuestoEmpleado


class PuestoSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar y editar datos de los
        Puestos. """
        
    class Meta:
        model  = Puesto
        fields = ['id', 'nombre']


class PuestoEmpleadoSerializer(serializers.ModelSerializer):
    """ Serializer para la relacion Puesto-Empleado. """
    id_puesto = serializers.ReadOnlyField(source='puesto.id')
    nombre = serializers.ReadOnlyField(source='puesto.nombre')
    puesto_id = serializers.PrimaryKeyRelatedField(
        queryset = Puesto.objects.all(),
        source = 'puesto',
        write_only = True,
    )

    class Meta:
        model  = PuestoEmpleado
        fields = [
            'id', 'id_puesto', 'nombre', 'puesto_id',
            'promocion', 'comentarios'
        ]


class PuestoEmpleadoReducedSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar datos reducidos del Puesto-Empleado """
    id = serializers.ReadOnlyField(source='puesto.id')
    nombre = serializers.ReadOnlyField(source='puesto.nombre')

    class Meta:
        model  = PuestoEmpleado
        fields = ['id', 'nombre',]