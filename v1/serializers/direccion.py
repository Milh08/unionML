from rest_framework import serializers

from ..models.direccion import Direccion
from ..models.persona import Persona


class DireccionSerializer(serializers.ModelSerializer):
    """ Serializer para listado general y específico. """
    persona_id = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        source='persona',
        write_only=True,
    )

    class Meta:
        model = Direccion
        fields = [
            'id', 'codigo_postal', 'pais', 'entidad', 'municipio',
            'ciudad', 'calle', 'tipo', 'persona_id',
        ]


class DireccionCreateRelatedSerializer(serializers.ModelSerializer):
    """
    Serializer para inserciones desde modelos relacionados:
    Ejemplo: Inserción desde Alumno.
    """
    class Meta:
        model = Direccion
        fields = [
            'id', 'codigo_postal', 'pais', 'entidad',
            'municipio', 'ciudad', 'calle',
        ]
