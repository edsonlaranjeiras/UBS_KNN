''''
Registrar no site do administrador
a tabela pessoas
'''
#from django.contrib import admin
#from .models import *
#admin.site.customizadaregister(Pessoa)

from django.contrib import admin
from .models import *

@admin.action(description="Habilitar Registros Selecionados") 
def habilitar_pessoas(ModelAdmin, request, queryset):
   queryset.update(ativo=True)

@admin.action(description="Desabilitar Registros Selecionados") 
def desabilitar_pessoas(ModelAdmin, request, queryset):
   queryset.update(ativo=False)

class PessoaCustomizado(admin.ModelAdmin):
   list_display = ('nome','funcao', 'email', 'celular','nascimento', 'calcula_idade', 'ativo',) 
   actions = [habilitar_pessoas, desabilitar_pessoas]
   
   
   @admin.display(description='Idade')
   def calcula_idade(self, obj):
      from datetime import date 
      hoje = date.today()
      idade = hoje.year - obj.nascimento.year
      
      # Ajusta a idade se o aniversário ainda não aconteceu neste ano
      if (hoje.month, hoje.day) < (obj.nascimento.month, obj.nascimento.day):
         idade -= 1
      return idade
   
admin.site.register(Pessoa, PessoaCustomizado)