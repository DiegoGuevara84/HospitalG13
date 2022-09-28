from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError('Los usuarios deben tener un nombre')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuario', primary_key=True, max_length = 25, null=False)
    password = models.CharField('Password', max_length = 256, unique=False, null=False)
    perfil = models.CharField('Perfil', max_length= 30, unique=False, null=False)
    nombre = models.CharField('Nombre', max_length = 35, unique=False, null=False)
    apellidos = models.CharField('Apellidos', max_length = 35, unique=False, null=False)
    telefonos = models.CharField('Telefono', max_length = 35, unique=False, null=False)
    genero = models.CharField('Genero', max_length = 35, unique=False, null=True)
    

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'