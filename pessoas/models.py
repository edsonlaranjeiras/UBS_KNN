from django.db import models
#Criando uma class pessoa
class Pessoa (models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='Email')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='celular')
    funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Funcao')
    nascimento = models.DateField(null=True, blank=True,verbose_name='Nascimento')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome','ativo',] # O Sinal - ordenar ascedente ou Descendente
            