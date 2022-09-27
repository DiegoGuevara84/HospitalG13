from appHG13.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('username_f', 'id_paciente', 'correo_', 'parentesco_f')