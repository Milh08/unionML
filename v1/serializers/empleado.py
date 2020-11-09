from rest_framework import serializers

# ------ MODELS ------
from ..models.empleado import Empleado
from ..models.direccion import Direccion
from ..models.categorias import CategoriaEmpleado
from ..models.division import DivisionEmpleado
from ..models.puesto import PuestoEmpleado
from ..models.sede import SedeEmpleado

# ------ SERIALIZERS ------
from .direccion import DireccionSerializer, DireccionCreateRelatedSerializer
from .categorias import CategoriaEmpleadoSerializer, CategoriaEmpleadoReducedSerializer
from .division import DivisionEmpleadoSerializer, DivisionEmpleadoReducedSerializer
from .puesto import PuestoEmpleadoSerializer, PuestoEmpleadoReducedSerializer
from .sede import SedeEmpleadoSerializer, SedeEmpleadoReducedSerializer


class EmpleadoCreateSerializer(serializers.ModelSerializer):
    """ Serializer para registrar un empleado nuevo. """
    direccion = DireccionCreateRelatedSerializer()

    sede = SedeEmpleadoSerializer(
        source='sedeempleado_set', many=True, allow_empty=False,
    )

    division = DivisionEmpleadoSerializer(
        source='divisionempleado_set', many=True, allow_empty=False,
    )

    puesto = PuestoEmpleadoSerializer(
        source='puestoempleado_set', many=True, allow_empty=False,
    )

    categoria = CategoriaEmpleadoSerializer(
        source='categoriaempleado_set', many=True, allow_empty=False,
    )

    class Meta:
        model  = Empleado
        fields = [
            'id', 'curp', 'nombre', 'apellido_paterno', 'apellido_materno',
            'sexo', 'estado_civil', 'fecha_nacimiento', 'nacionalidad', 'rfc',
            'nss', 'correo_electronico', 'telefono_casa', 'telefono_celular',
            'fecha_inicio', 'direccion', 'sede', 'division', 'puesto', 'categoria',
        ]
    
    def create(self, validated_data):
        direccion_data = validated_data.pop('direccion')
        sedes_data = validated_data.pop('sedeempleado_set')
        divisiones_data = validated_data.pop('divisionempleado_set')
        puestos_data = validated_data.pop('puestoempleado_set')
        categorias_data = validated_data.pop('categoriaempleado_set')

        empleado = Empleado.objects.create(**validated_data)

        direccion = Direccion.objects.create(
            persona=empleado, **direccion_data
        )

        for sede_data in sedes_data:
            SedeEmpleado.objects.create(empleado=empleado, **sede_data)

        for division_data in divisiones_data:
            DivisionEmpleado.objects.create(empleado=empleado, **division_data)

        for puesto_data in puestos_data:
            PuestoEmpleado.objects.create(empleado=empleado, **puesto_data)

        for categoria_data in categorias_data:
            CategoriaEmpleado.objects.create(empleado=empleado, **categoria_data)

        empleado.direccion = direccion
        return empleado


class EmpleadoUpdateSerializer(serializers.ModelSerializer):
    """ Serializer para actualizar los datos del empleado. """
    class Meta:
        model = Empleado
        fields = [
            'id', 'rfc', 'nss', 'correo_electronico',
            'telefono_casa', 'telefono_celular',
        ]


class EmpleadoListSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar los datos del empleado. """
    nombre = serializers.SerializerMethodField()
    division = DivisionEmpleadoReducedSerializer(source='divisionempleado_set', many=True)
    puesto = PuestoEmpleadoReducedSerializer(source='puestoempleado_set', many=True)
    sede = SedeEmpleadoReducedSerializer(source='sedeempleado_set', many=True)
    # categoria = CategoriaEmpleadoReducedSerializer(source='categoriaempleado_set', many=True)


    class Meta:
        model  = Empleado
        fields = ['id', 'nombre', 'puesto', 'sede', 'division']

    def get_nombre(self, obj):
        return '{} {} {}'.format(
            obj.nombre,
            obj.apellido_paterno,
            obj.apellido_materno
        )


class EmpleadoDetailSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar los datos del empleado. """
    nombre = serializers.SerializerMethodField()
    sede = SedeEmpleadoReducedSerializer(source='sedeempleado_set', many=True)
    division = DivisionEmpleadoReducedSerializer(source='divisionempleado_set', many=True)
    puesto = PuestoEmpleadoReducedSerializer(source='puestoempleado_set', many=True)
    categoria = CategoriaEmpleadoReducedSerializer(source='categoriaempleado_set', many=True)
    direccion = serializers.SerializerMethodField()


    class Meta:
        model  = Empleado
        fields = [
                'id', 'nombre', 'sede',
                'division', 'puesto', 'categoria',
                'direccion', 'antiguedad', 'edad',
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