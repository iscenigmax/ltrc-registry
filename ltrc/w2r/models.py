from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

    def __str__(self):
        return '{}'.format(self.nombre)


class Registro(models.Model):
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    TIEMPO_OBJETIVO = (
        (1, '15 a 20 minutos'),
        (2, '21 a 25 minutos'),
        (3, '26 a 30 minutos'),
        (4, '31 a 35 minutos'),
        (5, '+35 minutos'),
    )

    proyecto = models.ForeignKey(
        Proyecto,
        null=True,
        related_name='proyecto_%(class)s_objects',
        on_delete=models.SET_NULL
    )
    correo = models.EmailField()
    nombre = models.CharField(max_length=300)
    apellidos = models.CharField(max_length=300)
    edad = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXOS)
    peso_kgs = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=3, decimal_places=2)
    telefono = PhoneNumberField(blank=True, null=True)
    objetivo_5k = models.PositiveSmallIntegerField(choices=TIEMPO_OBJETIVO)
    tiempo_5k = models.CharField(max_length=8, blank=True, null=True)
    tiempo_10k = models.CharField(max_length=8,blank=True, null=True)
    tiempo_21k = models.CharField(max_length=8,blank=True, null=True)
    tiempo_42k = models.CharField(max_length=8,blank=True, null=True)
    confirmado = models.BooleanField('Acepto')
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"

    def __str__(self):
        return '{} {} - {}'.format(
            self.nombre,
            self.apellidos,
            self.get_objetivo_5k_display()
        )

    def get_absolute_url(self):
        return reverse('inicio', args=(self.pk,))

    def clean(self):
        try:
            if not self.confirmado:
                raise ValidationError({'confirmado': 'Debe aceptar los términos y condiciones.'})
        except Registro.DoesNotExist:
            pass