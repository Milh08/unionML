from rest_framework import serializers

from ..models.carrera import Carrera
from ..models.modalidad import Modalidad
from ..models.division import Division


class CarreraListSerializer(serializers.ModelSerializer):
    """ Serializer para listar todas las Carreras. """
    class Meta:
        model = Carrera
        fields = ['id', 'clave', 'nombre', 'nivel']
        # TODO
        # Many To Many [ Sedes -> Carreras ]


class CarreraCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar una Carrera. """
    modalidad_id = serializers.PrimaryKeyRelatedField(
        queryset=Modalidad.objects.all(),
        source='modalidad',
    )
    division_id = serializers.PrimaryKeyRelatedField(
        queryset=Division.objects.all(),
        source='division',
    )

    class Meta:
        model = Carrera
        fields = [
            'id', 'clave', 'clave_dgp', 'nombre', 'titulo', 'nivel',
            'periodicidad', 'vigencia', 'modalidad_id', 'division_id',
        ]


class CarreraRetrieveSerializer(serializers.ModelSerializer):
    """ Serializer para listar una sola Carrera. """
    class Meta:
        model = Carrera
        fields = [
            'id', 'clave', 'clave_dgp', 'nombre', 'nivel', 'titulo',
            # TODO
            # 'fecha_inicio'
        ]
