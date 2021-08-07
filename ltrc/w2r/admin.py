from django.contrib import admin
from import_export.admin import ExportMixin
from import_export.formats import base_formats

from ltrc.classes.manage_date import get_date_now_for_file
from w2r.models import Proyecto, Registro
from w2r.resources import RegistroResource


@admin.register(Proyecto)
class ClubAdmin(admin.ModelAdmin):
    pass


class RegistroAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RegistroResource
    save_on_top = True
    list_display = [
        'correo',
        'nombre',
        'apellidos',
        'edad',
        'sexo',
        'peso_kgs',
        'estatura',
        'objetivo_5k',
    ]
    ordering = ['id', ]

    def get_export_filename(self, file_format):
        return '{}.{}'.format(get_date_now_for_file(), file_format.get_extension())

    def get_export_formats(self):
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

    # tiempo_5k
    # tiempo_10k
    # tiempo_21k
    # tiempo_42k


admin.site.register(Registro, RegistroAdmin)

