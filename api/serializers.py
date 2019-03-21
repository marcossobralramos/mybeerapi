from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Marca, Modelo, Bebida, Produto, Loja, Cesta

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome')

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id', 'nome', 'volume')

class BebidaSerializer(serializers.HyperlinkedModelSerializer):
    marca = MarcaSerializer()
    modelo = ModeloSerializer()

    class Meta:
        model = Bebida
        fields = ('id', 'marca', 'modelo')

class LojaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loja
        fields = ('id', 'nome')

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    bebida = BebidaSerializer()
    loja = LojaSerializer()

    class Meta:
        model = Produto
        fields = ('id', 'bebida', 'loja', 'preco_unidade', 'preco_litro', 'ultima_atualizacao')

class CestaSerializer(serializers.HyperlinkedModelSerializer):
    produtos = ProdutoSerializer(many=True)
    
    class Meta:
        model = Cesta
        fields = ('id', 'descricao', 'total', 'litros', 'produtos')