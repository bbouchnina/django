from rest_framework import viewsets , status

from .serializers import ClientSerializer
from .models import Client
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self,request):
        queryset = Client.objects.all().order_by('nom')
        serializer_class=ClientSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def create(self,request):
        serializer_class = ClientSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
