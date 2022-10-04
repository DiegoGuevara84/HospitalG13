from django.db import models
from .user import User

class Psalud (models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad=models.CharField(max_length=45)
    rol = models.CharField(max_length=20)

