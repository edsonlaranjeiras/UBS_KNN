# Create your models here.
'''
Criando um model no DB para receber os valores que serão 
importados na APP ia_analise
'''
from django.db import models

class DatasetCancerBucal(models.Model):
    grupo = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name='Grupo')
    tabagismo = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Tabagismo')
    consumo_de_alcool = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Consumo de Álcool')
    idade = models.FloatField(null=True, blank=True, verbose_name='Idade')
    sexo = models.CharField(max_length=50, null=True,
                            blank=True, verbose_name='Sexo')
    infeccao_por_hpv = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Infecção por HPV')
    exposicao_solar = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Exposição Solar')
    dieta_inadequada = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Dieta Inadequada')
    higiene_bucal_inadequada = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Higiene Bucal Inadequada')
    uso_de_protese_inadequada = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Uso de Prótese Inadequada')
    grau_de_risco = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Grau de Risco')


def __str__(self):
    return self.grupo

class Meta:
    ordering = ['grupo']


class Pacientes(models.Model):
    grupo = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name='Grupo')
    Idade = models.FloatField(null=True, blank=True, verbose_name='Idade')
    Sexo = models.FloatField(null=True, blank=True, verbose_name='Sexo')
    Cond_Cancer = models.FloatField(
        null=True, blank=True, verbose_name='Cond_Cancer')
    Cond_Diabetes = models.FloatField(
        null=True, blank=True, verbose_name='Cond_Diabetes')
    Cond_Hipertensao = models.FloatField(
        null=True, blank=True, verbose_name='Cond_Hipertensao')
    Cond_Obesidade = models.FloatField(
        null=True, blank=True, verbose_name='Cond_Obesidade')
    Adm_Emergencia = models.FloatField(
        null=True, blank=True, verbose_name='Adm_Emergencia')
    Adm_Urgencia = models.FloatField(
        null=True, blank=True, verbose_name='Adm_Urgencia')
    Med_Ibuprofeno = models.FloatField(
        null=True, blank=True, verbose_name='Med_Ibuprofeno')
    Med_Lipitor = models.FloatField(
        null=True, blank=True, verbose_name='Med_Lipitor')
    Med_Paracetamol = models.FloatField(
        null=True, blank=True, verbose_name='Med_Paracetamol')
    Med_Penicilina = models.FloatField(
        null=True, blank=True, verbose_name='Med_Penicilina')
    Teste_Inconclusivo = models.FloatField(
        null=True, blank=True, verbose_name='Teste_Inconclusivo')
    Teste_Normal = models.FloatField(
        null=True, blank=True, verbose_name='Teste_Normal')
    Teste_Anormal = models.FloatField(
        null=True, blank=True, verbose_name='Teste_Anormal')


def __str__(self):
    return self.grupo

class Meta:
    ordering = ['grupo']


class Dados(models.Model):
    grupo = models.CharField(max_length=50, null=True, blank=True,
                             verbose_name='Grupo')
    mdw = models.FloatField(null=True, blank=True, verbose_name='mdw')
    latw = models.FloatField(null=True, blank=True, verbose_name='latw')
    tmcw = models.FloatField(null=True, blank=True, verbose_name='tmcw')
    racw = models.FloatField(null=True, blank=True, verbose_name='racw')
    araw = models.FloatField(null=True, blank=True, verbose_name='araw')
    mcw = models.FloatField(null=True, blank=True, verbose_name='mcw')
    psdsw = models.FloatField(null=True, blank=True, verbose_name='psdsw')
    s6w = models.FloatField(null=True, blank=True, verbose_name='s6w')
    mdr = models.FloatField(null=True, blank=True, verbose_name='mdr')
    latr = models.FloatField(null=True, blank=True, verbose_name='latr')
    tmcr = models.FloatField(null=True, blank=True, verbose_name='tmcr')
    racr = models.FloatField(null=True, blank=True, verbose_name='racr')
    arar = models.FloatField(null=True, blank=True, verbose_name='arar')
    mcr = models.FloatField(null=True, blank=True, verbose_name='mcr')
    psdsr = models.FloatField(null=True, blank=True, verbose_name='psdsr')
    s6r = models.FloatField(null=True, blank=True, verbose_name='s6r')
    mdg = models.FloatField(null=True, blank=True, verbose_name='mdg')
    latg = models.FloatField(null=True, blank=True, verbose_name='latg')
    tmcg = models.FloatField(null=True, blank=True, verbose_name='tmcg')
    racg = models.FloatField(null=True, blank=True, verbose_name='racg')
    arag = models.FloatField(null=True, blank=True, verbose_name='arag')
    mcg = models.FloatField(null=True, blank=True, verbose_name='mcg')
    psdsg = models.FloatField(null=True, blank=True, verbose_name='psdsg')
    s6g = models.FloatField(null=True, blank=True, verbose_name='s6g')
    mdwb = models.FloatField(null=True, blank=True, verbose_name='mdwb')
    latb = models.FloatField(null=True, blank=True, verbose_name='latb')
    tmcb = models.FloatField(null=True, blank=True, verbose_name='tmcb')
    racb = models.FloatField(null=True, blank=True, verbose_name='racb')
    arab = models.FloatField(null=True, blank=True, verbose_name='arab')
    mcb = models.FloatField(null=True, blank=True, verbose_name='mcb')
    psdsb = models.FloatField(null=True, blank=True, verbose_name='psdsb')
    s6b = models.FloatField(null=True, blank=True, verbose_name='s6b')


def __str__(self):
    return self.grupo


class Meta:
    ordering = ['grupo']
