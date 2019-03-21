from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Marca, Modelo, Bebida, Produto, Loja, Cesta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nome')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id', 'nome', 'volume')

class BebidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bebida
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(BebidaSerializer, self).to_representation(instance)
        representation['marca'] = MarcaSerializer(instance.marca).data
        representation['modelo'] = ModeloSerializer(instance.modelo).data
        return representation 

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('id', 'nome')

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'bebida', 'loja', 'preco_unidade', 'preco_litro', 'ultima_atualizacao')

    def to_representation(self, instance):
        representation = super(ProdutoSerializer, self).to_representation(instance)
        representation['bebida'] = BebidaSerializer(instance.bebida).data
        representation['loja'] = LojaSerializer(instance.loja).data
        return representation 

class CestaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cesta
        fields = ('id', 'descricao', 'total', 'litros', 'produtos')

    def to_representation(self, instance):
        representation = super(CestaSerializer, self).to_representation(instance)
        representation['produtos'] = ProdutoSerializer(instance.produtos, many=True).data
        return representation