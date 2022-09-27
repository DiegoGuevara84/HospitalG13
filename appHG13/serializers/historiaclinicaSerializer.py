from appHG13.models.histClinica import Historia_Clinica
from rest_framework import serializers

class Historia_ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_Clinica
        fields = ('hc_Paciente', 'hc_Fecha', 'hc_Entorno', 'hc_Diagnostico', 'hc_Recomendaciones')