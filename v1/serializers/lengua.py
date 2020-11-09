from rest_framework import serializers

from ..models.lengua import Lengua, PersonaLengua


class LenguaSerializer(serializers.ModelSerializer):
    """ Serializer para listado general y específico. """
    class Meta:
        model = Lengua
        fields = [
            'id', 'nombre', 'alias', 'familia', 'agrupacion',
            'originaria', 'extranjera', 'materia',
        ]


class PersonaLenguaSerializer(serializers.ModelSerializer):
    """ Serializer para relación Persona-Lenguas. """
    id = serializers.ReadOnlyField(source='lengua.id')
    nombre = serializers.ReadOnlyField(source='lengua.nombre')
    lengua_id = serializers.PrimaryKeyRelatedField(
        queryset=Lengua.objects.all(),
        source='lengua',
        write_only=True,
    )

    class Meta:
        model = PersonaLengua
        fields = [
            'id', 'nombre', 'lengua_id', 'read', 'listening',
            'written', 'speaking', 'tipo', 'comentarios',
        ]
