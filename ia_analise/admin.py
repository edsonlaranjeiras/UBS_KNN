# Register your models here.

from django.contrib import admin
from .models import DatasetCancerBucal

@admin.register(DatasetCancerBucal)
class DatasetCancerBucalAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'tabagismo', 'consumo_de_alcool', 'idade', 'sexo', 'infeccao_por_hpv', 'exposicao_solar', 'dieta_inadequada', 'higiene_bucal_inadequada', 'uso_de_protese_inadequada', 'grau_de_risco')
    search_fields = ('grupo', 'sexo', 'grau_de_risco')  # Campos que podem ser pesquisados
    list_filter = ('sexo', 'grau_de_risco')  # Filtros laterais
