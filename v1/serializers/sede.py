from rest_framework import serializers

from ..models.sede import Sede, SedeEmpleado


class SedeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = [
            'id', 'clave', 'nombre',
            # TODO
            # carreras (id, nombre)
        ]


class SedeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        exclude = [
            'entidad', 'pais',
            'created_at', 'updated_at', 'deleted_at',
        ]


class SedeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = [
            'id', 'clave', 'nombre', 'ciudad',
            'municipio',
            # TODO
            # carreras (id, nombre)
            # edificios (id, nombre)
            # espacios (id, nombre)
        ]


class SedeEmpleadoSerializer(serializers.ModelSerializer):
    """ Serializer para la relacion Sede-Empleado """
    id_sede = serializers.ReadOnlyField(source='sede.id')
    nombre = serializers.ReadOnlyField(source='sede.nombre')
    sede_id = serializers.PrimaryKeyRelatedField(
        queryset = Sede.objects.all(),
        source = 'sede',
        write_only = True,
    )

    class Meta:
        model = SedeEmpleado
        fields = [
            'id', 'id_sede', 'nombre', 'sede_id',
            'promocion', 'comentarios'
        ]


class SedeEmpleadoReducedSerializer(serializers.ModelSerializer):
    """ Serializer para la relacion Sede-Empleado """
    id = serializers.ReadOnlyField(source='sede.id')
    nombre = serializers.ReadOnlyField(source='sede.nombre')

    class Meta:
        model = SedeEmpleado
        fields = ['id', 'nombre',]