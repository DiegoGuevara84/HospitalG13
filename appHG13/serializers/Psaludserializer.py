from appHG13.models import Psalud
from appHG13.models.Psalud import Personal_salud
from rest_framework import serializers

class Personal_SaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psalud
        fields = ('username', 'rol', 'especialidad')