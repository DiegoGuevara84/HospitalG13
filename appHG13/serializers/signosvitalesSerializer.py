from appHG13.models.signosVitales import Signos_Vitales
from rest_framework import serializers

class Signos_VitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signos_Vitales
        fields = ('sv_paciente', 'sv_oximetria', 'sv_f_respiratoria', 'sv_f_cardiaca', 'sv_temperatura', 'sv_presion_arterial', 'sv_glicemia')