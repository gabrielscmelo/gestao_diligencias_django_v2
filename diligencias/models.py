from django.db import models

class Diligencias(models.Model):
    saj = models.CharField("SAJ", max_length=50, null=False, blank=False)
    diligencia = models.CharField("Diligência", max_length=255, null=False, blank=False)
    data_envio = models.DateTimeField("Envio", auto_now_add=True)
    sei = models.CharField("SEI", max_length=50, null=False, blank=False)
    secretaria = models.CharField("Secretaria", max_length=50, null=False, blank=False)
    prazo = models.DateField("Prazo", null=True, blank=True)
    resposta = models.TextField("Resposta", null=True, blank=True)
    inserido = models.DateField("Inserido", null=True, blank=True)
    prazo_do_bloco_de_status = models.DateField("Prazo do bloco de Status", null=True, blank=True)
    status = models.CharField("Status", default="PENDENTE")
    cobranca = models.DateField("Cobrança", null=True, blank=True)
    proxima_cobranca = models.DateField("Proxima cobrança", null=True, blank=True)

    def __str__(self):
        return self.diligencia

# Create your models here.
