from django.views.generic import ListView

from diligencias.models import Diligencia

class DiligenciaListView(ListView):
    model = Diligencia

# Create your views here.
