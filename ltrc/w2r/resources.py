#!/usr/bin/python
# -*- encoding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import BooleanWidget
from .models import Registro
__author__ = 'csanchez'
__date__ = '2019/11/06 22:58'


class RegistroResource(resources.ModelResource):
    class Meta:
        model = Registro
        fields = (
            'id',
            'correo',
            'nombre',
            'apellidos',
            'edad',
            'sexo',
            'peso_kgs',
            'estatura',
            'objetivo_5k',
        )

