#!/usr/bin/python
# -*- encoding: utf-8 -*-
from import_export import resources
from registro.models import Corredor

__author__ = 'csanchez'
__date__ = '2018/12/20 23:40'


class CorredorResource(resources.ModelResource):
    class Meta:
        model = Corredor
        fields = (
            'id', 'nombre', 'apellido_paterno', 'apellido_materno', 'club', 'sexo', 'telefono', 'correo', 'talla',
            'confirmado',
        )
