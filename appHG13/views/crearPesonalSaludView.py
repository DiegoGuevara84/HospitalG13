#from urllib import request
from rest_framework import status,views
from rest_framework.response import Response
from appHG13.serializers.Psaludserializer import Personal_SaludSerializer

class CrearPersonalSaludView(views.APIView):
    def post(self,request):
        serializer=Personal_SaludSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)