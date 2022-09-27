from django.db import models
from .user import User
from .paciente import Paciente
from appHG13.models import user

class Familiar(models.Model):
    id_f = models.AutoField('ID familiar', primary_key=True, null=False)
    username_f = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE,max_length=30, null=False)
    id_paciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE, null=False)
    correo_f = models.EmailField('Correo familiar', max_length=50, unique=True, null=False)
    parentesco_f = models.CharField('Parentesco familiar', max_length=20, unique=False, null=False)