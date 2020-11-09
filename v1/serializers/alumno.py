from rest_framework import serializers

from ..models.alumno import Alumno
from ..models.categorias import CategoriaAlumno
from ..models.direccion import Direccion
from ..models.lengua import PersonaLengua
from .direccion import (DireccionSerializer,
                        DireccionCreateRelatedSerializer)
from .lengua import PersonaLenguaSerializer


class AlumnoListSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar los datos del alumno. """
    nombre = serializers.SerializerMethodField()
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaAlumno.objects.all(),
        source='categoria',
    )
    direccion = serializers.SerializerMethodField()
    lenguas = PersonaLenguaSerializer(source='personalengua_set', many=True)

    class Meta:
        model = Alumno
        fields = [
            'id', 'nombre', 'curp', 'sexo', 'nss',
            'categoria_id', 'direccion', 'edad', 'lenguas',
        ]

    def get_nombre(self, obj):
        return '{} {} {}'.format(
            obj.nombre,
            obj.apellido_paterno,
            obj.apellido_materno
        )

    def get_direccion(self, obj):
        latest = obj.direcciones.all().latest('created_at')
        serializer = DireccionSerializer(instance=latest)
        return {
            'ciudad': serializer.data['ciudad'],
            'calle': serializer.data['calle'],
        }


class AlumnoCreateSerializer(serializers.ModelSerializer):
    """ Serializer para registrar un nuevo alumno. """
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaAlumno.objects.all(),
        source='categoria',
    )
    direccion = DireccionCreateRelatedSerializer()
    lenguas = PersonaLenguaSerializer(
        source='personalengua_set', many=True, allow_empty=False,
    )

    class Meta:
        model = Alumno
        fields = [
            'id', 'curp', 'nombre', 'apellido_paterno', 'apellido_materno',
            'sexo', 'estado_civil', 'fecha_nacimiento', 'nacionalidad', 'rfc',
            'nss', 'correo_electronico', 'telefono_casa', 'telefono_celular',
            'categoria_id', 'direccion', 'lenguas',
        ]

    def create(self, validated_data):
        direccion_data = validated_data.pop('direccion')
        lenguas_data = validated_data.pop('personalengua_set')

        alumno = Alumno.objects.create(**validated_data)

        direccion = Direccion.objects.create(
            persona=alumno, **direccion_data
        )

        for lengua_data in lenguas_data:
            PersonaLengua.objects.create(persona=alumno, **lengua_data)

        # Es necesario agregar el atributo dirección ya que
        # por defecto no existe en alumno. De otro modo la
        # vista de creación lanza AttributeError.
        alumno.direccion = direccion
        return alumno


class AlumnoUpdateSerializer(serializers.ModelSerializer):
    """ Serializer para actualizar los datos del alumno. """
    class Meta:
        model = Alumno
        fields = [
            'id', 'rfc', 'nss', 'correo_electronico',
            'telefono_casa', 'telefono_celular',
        ]
