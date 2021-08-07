# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from ltrc.classes.manage_choices import year_choices
from ltrc.classes.manage_date import get_current_year


class ThenEnd(models.Model):
    anio = models.IntegerField(_('año'), null=False, blank=False, choices=year_choices(), default=get_current_year)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['anio', ]
        verbose_name = "ThenEnd"
        verbose_name_plural = "ThenEnds"

    def __str__(self):
        return '{}'.format(self.anio)


class Club(models.Model):
    nombre = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['nombre', ]
        verbose_name = "club"
        verbose_name_plural = "clubes"
        ordering = ['nombre']

    def __str__(self):
        return '{}'.format(self.nombre)


class Corredor(models.Model):

    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    TALLAS = (
        ('CH', 'CH'),
        ('M', 'M'),
        ('G', 'G'),
    )

    club = models.ForeignKey(
        Club,
        null=True,
        related_name='club_%(class)s_objects',
        on_delete=models.SET_NULL
    )
    the_end = models.ForeignKey(
        ThenEnd,
        null=True,
        related_name='ThenEnd_%(class)s_objects',
        on_delete=models.SET_NULL
    )

    guia = models.CharField('Guia TALAMAS', max_length=20, null=True, blank=True, unique=True)
    folio = models.CharField(max_length=4, null=True, blank=True)
    nombre = models.CharField(max_length=300)
    apellido_paterno = models.CharField(max_length=300)
    apellido_materno = models.CharField(max_length=300)
    fecha_nacimiento = models.DateTimeField()
    sexo = models.CharField(max_length=1, choices=SEXOS)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField()
    talla = models.CharField(max_length=2, choices=TALLAS)
    confirmado = models.BooleanField('Acepto términos y condiciones')
    asistencia = models.BooleanField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['correo', 'the_end']
        verbose_name = "corredor"
        verbose_name_plural = "corredores"
        ordering = ('pk',)

    def __str__(self):
        return '{} {} {} - {}'.format(self.nombre, self.apellido_paterno, self.apellido_materno, self.club)

    def clean(self):
        try:
            if not self.confirmado:
                raise ValidationError({'confirmado': 'Debe aceptar los términos y condiciones.'})
            if not self.guia:
                raise ValidationError({'guia': 'Debe proporcionar la guía del folio.'})
            if not (self.guia.startswith('CORTESIA-') or self.guia.startswith('LTRC-')) and not self.pk:
                if len(self.guia) != 5 or int(self.guia) < 67893:
                    raise ValidationError({'guia': 'El número de guía no es correcto.'})
        except Corredor.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        if not self.pk:
            anio = ThenEnd.objects.get(anio=get_current_year())
            self.the_end = anio
            self.guia = '{}-{}'.format(self.the_end, self.guia)
            # self.folio = (int(
            #                 Corredor.objects.filter(
            #                     the_end__id__exact=6
            #                 ).filter(~Q(folio=None)).extra(select={'myinteger': 'CAST(folio AS INTEGER)'}).last().folio
            #             ) + 1)
        super(Corredor, self).save(*args, **kwargs)
