from rest_framework import viewsets , status

from .serializers import ClientSerializer , ProduitSerializer
from .models import Client , Produit
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


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


class ProduitViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self,request):
        queryset = Produit.objects.all().order_by('libelle')
        serializer_class=ProduitSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def retrieve(self,request,pk=None):
        # queryset = Produit.objects.all()
        produit = get_object_or_404(Produit,pk=pk)
        serializer_class=ProduitSerializer(produit)
        return Response(serializer_class.data)
    def create(self,request):
        serializer_class = ProduitSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        produit = get_object_or_404(Produit,pk=pk)
        serializer_class=ProduitSerializer(produit,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
