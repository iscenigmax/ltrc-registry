from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from registro.views import registrado, confirmacion, corredor, CorredorListView
from inicio.views import inicio

admin.autodiscover()

admin.site.site_title = "Sistema de administracion"
admin.site.site_header = "ICONS.CLOUD"
admin.site.index_title = "ICONS.CLOUD"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('registrado/<int:id>/', registrado, name='registrado'),
    path('confirmacion/<int:id>/', confirmacion, name='confirmacion'),
    # path('asistio/<int:id>/', asistio, name='asistio'),
    # path('no/asistio/<int:id>/', no_asistio, name='asistio'),
    path('terminos/', TemplateView.as_view(template_name='aviso_privacidad.html'), name='terminos'),
    path('ruta/', TemplateView.as_view(template_name='ruta.html') , name='ruta'),
    # path('encuestas/<int:folio>/', encuesta, name='encuesta'),
    path('registro/corredor/create/', corredor, name='registro_corredor_create'),
    path('registro/corredor/', CorredorListView.as_view(), name='reistro_corredor_list'),
    # path('w2r/registro/create/', RegistroCreateView.as_view(), name='w2r_registro_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
