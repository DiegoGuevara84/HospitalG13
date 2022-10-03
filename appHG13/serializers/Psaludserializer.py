from string import printable
from rest_framework import serializers
from appHG13.models.Psalud import Psalud

class Psaludserializer(serializers.ModelSerializer):
    class Meta:
        model = Psalud
        fields = ['id', 'especialidad', 'registro', 'usuario']

"""from appHG13.models import Psalud
from appHG13.models.Psalud import Personal_salud
from rest_framework import serializers

class Personal_SaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psalud
        fields = ('id_Psalud','username', 'rol', 'especialidad')"""