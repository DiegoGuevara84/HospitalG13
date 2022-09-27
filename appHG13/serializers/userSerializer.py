from rest_framework import serializers
from appHG13.models.user import User
from appHG13.models.account import Account
from appHG13.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['username', 'password', 'perfil', 'nombre', 'apellidos', 'telefono', 'genero']

    
