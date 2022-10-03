from django.db import models
from .user import User

class Personal_salud(models.Model):
    id_Psalud = models.AutoField('ID PersonalSalud',primary_key=True, null=False)
    username = models.ForeignKey(User, related_name='Psalud', on_delete=models.CASCADE, max_length=30, null=False)
    rol = models.CharField('Rol', max_length=35,unique=False, null=False)
    especialidad=models.CharField('Especialidad', max_length=35, unique=False, null=False)