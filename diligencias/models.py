from django.db import models

class Diligencia(models.Model):
    saj = models.CharField("SAJ", max_length=50, blank=True)
    diligencia = models.CharField("Diligência", max_length=255)
    data_envio = models.DateField("Envio", null=True, blank=True)
    sei = models.CharField("SEI", max_length=50, null=False, blank=True)
    secretaria = models.CharField("Secretaria", max_length=100, null=False, blank=True)
    prazo = models.DateField("Prazo", null=True, blank=True)
    resposta = models.TextField("Resposta", null=True, blank=True)
    inserido = models.DateField("Inserido", null=True, blank=True)
    prazo_do_bloco_de_status = models.DateField("Prazo do bloco de Status", null=True, blank=True)
    status = models.CharField("Status", default="PENDENTE")
    cobranca = models.DateField("Cobrança", null=True, blank=True)
    proxima_cobranca = models.DateField("Proxima cobrança", null=True, blank=True)

    def __str__(self):
        return self.diligencia

