from django import forms

from diligencias.models import Diligencia


class DiligenciaForm(forms.ModelForm):
    class Meta:
        model = Diligencia
        fields = ["saj", "sei", "diligencia", "data_envio", "secretaria", "prazo", "respondido"]
        widgets = {
            "data_envio": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "prazo": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "prazo_do_bloco_de_status": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "cobranca": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }