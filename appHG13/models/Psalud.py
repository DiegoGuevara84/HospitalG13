from django.db import models
from .user import User

class Psalud (models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad=models.CharField(max_length=45)
    registro = models.CharField(max_length=20)

"""from django.db import models
from .user import User

class Personal_salud(models.Model):
    id_Psalud = models.AutoField('ID PersonalSalud',primary_key=True)
    username = models.ForeignKey(User, related_name='Psalud', on_delete=models.CASCADE)
    rol = models.CharField('Rol', max_length=35)
    especialidad=models.CharField('Especialidad', max_length=35)"""