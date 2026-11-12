from django.db import models



class Diligencia(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        CONCLUIDO = "CONCLUÍDO", "Concluído"


    saj = models.CharField("SAJ", max_length=50, blank=True)
    diligencia = models.CharField("Diligência", max_length=255)
    data_envio = models.DateField("Envio", null=True, blank=True)
    sei = models.CharField("SEI", max_length=50, null=False, blank=True)
    secretaria = models.CharField("Secretaria", max_length=100, null=False, blank=True)
    prazo = models.DateField("Prazo", null=True, blank=True)
    resposta = models.TextField("Resposta", null=False, blank=True)
    inserido = models.DateField("Inserido", null=True, blank=True)
    prazo_do_bloco_de_status = models.DateField("Prazo do bloco de Status", null=True, blank=True)
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.PENDENTE)
    cobranca = models.DateField("Cobrança", null=True, blank=True)
    proxima_cobranca = models.DateField("Próxima cobrança", null=True, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

class Meta:
    verbose_name = "diligência"
    verbose_name_plural = "diligências"

 

    def __str__(self):
        return self.diligencia

