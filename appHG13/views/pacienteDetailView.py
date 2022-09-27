from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from appHG13.models.paciente import Paciente
from appHG13.serializers.pacienteSerializer import PacienteSerializer
class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    

    def get(self, request, *args, **kwargs):


 

        return super().get(request, *args, **kwargs)