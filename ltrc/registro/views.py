# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.generic import ListView

from .models import Corredor
from .forms import CorredorForm
from django.contrib import messages


class CorredorListView(ListView):
    model = Corredor

    def get_queryset(self):
        # queryset = Corredor.objects.none()
        queryset = Corredor.objects.filter(
            Q(the_end__anio=2019) & ~Q(folio=None)
        ).extra(select={'myinteger': 'CAST(folio AS INTEGER)'}).order_by('myinteger')
        if self.request.GET.get("filter"):
            # guia = self.request.GET.get("filter")
            # queryset = Corredor.objects.filter(the_end__anio=2019)
            # queryset = queryset.filter(guia='2019-'+guia)
            filtro = self.request.GET.get("filter")
            # queryset = Corredor.objects.filter(the_end__anio=2019)
            queryset = queryset.filter(Q(nombre__icontains=filtro) | Q(apellido_paterno__icontains=filtro))
        return queryset[:250]


def corredor(request):
    template_name = 'registro/corredor_form.html'
    form = CorredorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                c = form.save()
                return HttpResponseRedirect(reverse('confirmacion', args=(c.pk,)))
            except Exception as e:
                messages.add_message(request, messages.ERROR, str(e))
    return render(request, template_name, {'form': form})


def registrado(request, id):
    mensaje_error = ''
    mensaje = ''
    try:
        corredor = Corredor.objects.get(id=id)
        subject = 'Registro {} - {} - {}'.format(corredor.guia, corredor.nombre, corredor.club.nombre)
        html_message = """
            <p>
            Tu registro con guia [{}] fue realizado con éxito, para concluir y validar que los datos sean correctos
            favor de <a href="https://ltrc.herokuapp.com/confirmacion/{}/">DAR CLICK AQUÍ</a>, gracias.
            <p/>
            <p>
            En caso de corrección de datos, dudas o soporte enviar a <a href="mailto:ing.casr@gmail.com">ICONS</a>.
            </p>
        """.format(corredor.guia, str(id))
        plain_message = strip_tags(html_message)
        from_email = 'no-replay@icons.com'
        to = corredor.correo

        # try:
        #     send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=False)
        # except:
        #     pass

        corredor.confirmado = False
        corredor.save()

        mensaje = """
            <h4>GUIA: {}</h4>
            Felicidades solo un paso más {}, se te enviará tu confirmación vía correo para activarlo.""".format(
        corredor.guia,
        corredor.nombre.upper())
    except Corredor.DoesNotExist:
        mensaje_error = 'Registro NO encontrado'

    return render(request, 'inicio.html', {'mensaje': mensaje, 'mensaje_error': mensaje_error})


def confirmacion(request, id):
    imprimir = False
    try:
        corredor = Corredor.objects.get(id=id)
        corredor.confirmado = True
        corredor.save()
        mensaje = """
        <h4 class='text-center'>PRESENTAR LA PANTALLA Y TICKET AL RECOGER EL KIT</h4>
        <br/>
        <p>Felicidades {} has sido correctamente registrado para la carrera mas esperada del año THE END V.</p>
        <br/>
        <table class="table table-condensed table-bordered">
        <caption class="text-center">REGISTRO</caption>
        <tr>
            <td><strong>Guia:</strong></td>
            <td>{}</td>
        </tr>
        <tr>
            <td><strong>Nombre:</strong></td>
            <td>{}</td>
        </tr>
        <tr>
            <td><strong>Talla:</strong></td>
            <td>{}</td>
        </tr>
        <tr>
            <td><strong>Club:</strong></td>
            <td>{}</td>
        </tr>""".format(
            corredor.nombre,
            corredor.guia,
            '{} {} {}'.format(corredor.nombre, corredor.apellido_paterno, corredor.apellido_materno),
            corredor.talla,
            corredor.club,
        )

        imprimir = True
        mensaje += """
        </table>
        <p>Confirmo que acepte los términos y condiciones para el evento de THE END V y recogere el kit en la hora 
        y lugar que el organizar notifique días previo al evento.</p>
        """
    except Corredor.DoesNotExist:
        mensaje = 'Registro NO encontrado'
    return render(request, 'inicio.html', {'mensaje': mensaje, 'imprimir': imprimir})


def asistio(request, id):
    try:
        corredor = Corredor.objects.get(id=id)
        corredor.asistencia = True
        corredor.save()
        mensaje = """
        Guia: {} - Nombre: {} <b style="color:lime">CONFIRMACION DE ASISTENCIA REALIZADA</b>
        """.format(corredor.guia, corredor.nombre)
    except Corredor.DoesNotExist:
        mensaje = 'Guia: {} <b sytle="color:red">NO ENCONTRADO</b>'.format(corredor.guia)

    return HttpResponse(mensaje)


def no_asistio(request, id):
    try:
        corredor = Corredor.objects.get(id=id)
        corredor.asistencia = False
        corredor.save()
        mensaje = """
            Guia: {} - Nombre: {} 
            <b style="color:lime">CONFIRMACION <b style="color:red">NO</b> 
            DE ASISTENCIA REALIZADA</b>
        """.format(corredor.guia, corredor.nombre)
    except Corredor.DoesNotExist:
        mensaje = 'Guia: {} <b sytle="color:red">NO ENCONTRADO</b>'.format(id)

    return HttpResponse(mensaje)
