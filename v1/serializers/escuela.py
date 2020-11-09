from rest_framework import serializers

from ..models.escuela import Escuela


class EscuelaSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar datos de Escuelas. """
    class Meta:
        model = Escuela
        fields = [
            'id', 'cct', 'nombre', 'acronimo', 'plantel',
            'is_num', 'nivel', 'tipo', 'grado', 'sector',
            'municipio', 'entidad', 'pais',
        ]
