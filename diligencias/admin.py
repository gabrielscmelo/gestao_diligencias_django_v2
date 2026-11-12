from django.contrib import admin

from diligencias.models import Diligencia


@admin.register(Diligencia)
class DiligenciaAdmin(admin.ModelAdmin):
    list_display = ("diligencia", "status", "saj", "sei", "secretaria", "prazo")
    list_filter = ("status", "secretaria")
    search_fields = ("diligencia", "saj", "sei","secretaria")
    readonly_fields = ("criado_em", )
