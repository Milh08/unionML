from django.urls import path

from .views.sede import SedeList, SedeDetails
from .views.persona import PersonaList, PersonaDetails
from .views.alumno import AlumnoList, AlumnoDetails
from .views.categorias import (CategoriaList, CategoriaDetails,
                                CategoriaAlumnoList, CategoriaAlumnoDetails,
                                CategoriaEmpleadoList, CategoriaEmpleadoDetails)
from .views.direccion import DireccionList, DireccionDetails
from .views.lengua import LenguaList, LenguaDetails
from .views.carrera import CarreraList, CarreraDetails
from .views.escuela import EscuelaList, EscuelaDetails
from .views.division import DivisionList, DivisionDetails
from .views.modalidad import ModalidadList, ModalidadDetails
from .views.empleado import EmpleadoList, EmpleadoDetails
from .views.puesto import (PuestoList, PuestoDetails,
                            PuestoEmpleadoList, PuestoEmpleadoDetails)

urlpatterns = [  # pk -> id
    path('personas/', PersonaList.as_view()),
    path('personas/<int:pk>', PersonaDetails.as_view()),
    path('alumnos/', AlumnoList.as_view()),
    path('alumnos/<int:pk>', AlumnoDetails.as_view()),
    # ---- CATEGORIAS ----
    path('categorias/', CategoriaList.as_view()),
    path('categorias/<int:pk>', CategoriaDetails.as_view()),
    path('alumnos/categorias/', CategoriaAlumnoList.as_view()),
    path('alumnos/categorias/<int:pk>', CategoriaAlumnoDetails.as_view()),
    # path('empleado/categoria/', CategoriaEmpleadoList.as_view()),
    # path('empleado/categoria/<int:pk>', CategoriaEmpleadoDetails.as_view()),
    path('direcciones/', DireccionList.as_view()),
    path('direcciones/<int:pk>', DireccionDetails.as_view()),
    path('lenguas/', LenguaList.as_view()),
    path('lenguas/<int:pk>', LenguaDetails.as_view()),
    path('sedes/', SedeList.as_view()),
    path('sedes/<int:pk>', SedeDetails.as_view()),
    path('carreras/', CarreraList.as_view()),
    path('carreras/<int:pk>', CarreraDetails.as_view()),
    path('escuelas/', EscuelaList.as_view()),
    path('escuelas/<int:pk>', EscuelaDetails.as_view()),
    # ---- DIVICION ----
    path('divisiones/', DivisionList.as_view()),
    path('divisiones/<int:pk>', DivisionDetails.as_view()),

    path('modalidades/', ModalidadList.as_view()),
    path('modalidades/<int:pk>', ModalidadDetails.as_view()),
    # ---- EMPLEADO ----
    path('empleado/', EmpleadoList.as_view()),
    path('empleado/<int:pk>', EmpleadoDetails.as_view()),
    # ---- PUESTO ----
    path('puestos/', PuestoList.as_view()),
    path('puestos/<int:pk>', PuestoDetails.as_view()),
    # path('empleado/puesto/', PuestoEmpleadoList.as_view()),
    # path('empleado/puesto/<int:pk>', PuestoEmpleadoDetails.as_view()) 
]
