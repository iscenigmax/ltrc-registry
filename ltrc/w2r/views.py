from django.views.generic import CreateView

from w2r.forms import RegistroForm
from w2r.models import Registro


class RegistroCreateView(CreateView):
    model = Registro
    form_class = RegistroForm
