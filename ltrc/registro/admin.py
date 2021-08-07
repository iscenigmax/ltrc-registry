# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.formats import base_formats
from ltrc.classes.manage_date import get_date_now_for_file
from registro.resources import CorredorResource
from import_export.admin import ExportMixin
from .models import Club, Corredor, ThenEnd


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Corredor)
class CorredorAdmin(ExportMixin, admin.ModelAdmin):
    save_on_top = True
    list_display = [
        'id', 'guia', 'folio', 'talla', 'nombre', 'apellido_paterno', 'apellido_materno', 'club', 'sexo', 'the_end'
    ]
    search_fields = ('nombre', 'folio', 'guia')
    list_filter = ('the_end', )
    ordering = ('id',)

    def get_export_filename(self, file_format):
        return '{}.{}'.format(get_date_now_for_file(), file_format.get_extension())

    def get_export_formats(self):
        formats = (
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


@admin.register(ThenEnd)
class ThenEndAdmin(admin.ModelAdmin):
    pass