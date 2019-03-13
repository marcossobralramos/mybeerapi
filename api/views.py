from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Marca, Modelo, Loja, Bebida, Produto, Cesta
from api.serializers import MarcaSerializer, ModeloSerializer, LojaSerializer, BebidaSerializer, ProdutoSerializer, CestaSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CestaViewSet(viewsets.ModelViewSet):
    queryset = Cesta.objects.all()
    serializer_class = CestaSerializer