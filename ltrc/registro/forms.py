#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from django.forms import TextInput

from .models import Corredor
__author__ = 'csanchez'
__date__ = '2018/11/20 22:00'


class CorredorForm(forms.ModelForm):
    class Meta:
        model = Corredor
        fields = [
            'guia',
            'nombre', 'apellido_paterno', 'apellido_materno',
            'fecha_nacimiento',
            'sexo',
            'telefono',
            'colonia',
            'correo',
            'talla',
            'club',
            'confirmado'
        ]

        widgets = {
            'fecha_nacimiento': TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
