from django.db import models
from .user import User
from .Psalud import Personal_salud

class Paciente (models.Model):
    p_id = models.AutoField('ID paciente', primary_key=True, null=False)
    p_username = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    p_personal_salud = models.ForeignKey(Personal_salud, related_name='paciente', on_delete=models.CASCADE)
    p_fecha_nacimiento = models.DateField('Fecha nacimiento paciente', unique=False, null=False)
    p_ciudad = models.CharField('Ciudad paciente', max_length=20, unique=False, null=False)
    p_direccion = models.CharField('Direccion paciente', max_length=40, unique=False, null=False)
   