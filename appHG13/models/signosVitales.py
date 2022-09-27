from django.db import models
from .paciente import Paciente

class Signos_Vitales(models.Model):
    sv_id = models.AutoField('ID signos vitales', primary_key=True, null=False)
    sv_paciente = models.ForeignKey(Paciente, related_name='signos_vitales', on_delete=models.CASCADE, unique=False, null=False)
    sv_fecha_hora = models.DateTimeField('Fecha hora signos vitales', auto_now=True, unique=False, null=False)
    sv_oximetria = models.FloatField('Oximetría', unique=False, null=True)
    sv_f_respiratoria = models.FloatField('Frecuencia respiratoria', unique=False, null=True)
    sv_f_cardiaca = models.FloatField('Frecuencia cardíaca', unique=False, null=True)
    sv_temperatura = models.FloatField('Temperatura', unique=False, null=True)
    sv_presion_arterial = models.FloatField('Presión arterial', unique=False, null=True)
    sv_glicemia = models.FloatField('Glicemia', unique=False, null=True)