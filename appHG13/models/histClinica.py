from django.db import models
from .paciente import Paciente

class Historia_Clinica(models.Model):
    hc_Id = models.AutoField('Id historia clinica', primary_key=True, null=False)
    hc_Paciente = models.ForeignKey(Paciente, related_name='historia_clinica', on_delete=models.CASCADE, unique=False, null=False)
    hc_Fecha = models.DateTimeField('Fecha historia clinica', auto_now=True, unique=False, null=False)
    hc_Entorno = models.CharField('Entorno', max_length=50, unique=False, null=False)
    hc_Diagnostico = models.CharField('Diagnsstico', max_length=100, unique=False, null=False)
    hc_Recomendaciones = models.CharField('Recomendaciones', max_length=200, unique=False, null=False)