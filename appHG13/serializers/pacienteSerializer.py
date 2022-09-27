from appHG13.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('username', 'id_Psalud', 'p_fecha_nacimiento', 'ciudad', 'direccion')