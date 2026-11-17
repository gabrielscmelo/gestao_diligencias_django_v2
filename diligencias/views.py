from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from diligencias.models import Diligencia
from diligencias.forms import DiligenciaForm

class DiligenciaListView(ListView):
    model = Diligencia

class DiligenciaCreateView(CreateView):
    model = Diligencia
    form_class = DiligenciaForm
    success_url = reverse_lazy("diligencias:lista")

class DiligenciaUpdateView(UpdateView):
    model = Diligencia
    form_class = DiligenciaForm
    success_url = reverse_lazy("diligencias:lista")

