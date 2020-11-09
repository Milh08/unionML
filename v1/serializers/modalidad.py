from rest_framework import serializers

from ..models.modalidad import Modalidad


class ModalidadSerializer(serializers.ModelSerializer):
    """
    Serializer para crear, visualizar y actualizar Modalidades.
    """
    class Meta:
        model = Modalidad
        fields = ['id', 'nombre']
