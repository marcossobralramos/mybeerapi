from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Marca, Modelo, Bebida, Produto, Loja, Cesta, ProdutosCesta

import json

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
    produtos = serializers.ListField()

    class Meta:
        model = Cesta
        fields = ('id', 'descricao', 'total', 'litros', 'produtos')

    def create(self, validated_data):
        produtos = validated_data.pop('produtos')
        cesta = Cesta.objects.create(**validated_data)

        for produto in produtos:
            produto_cesta = ProdutosCesta(
                produto=Produto.objects.get(id=produto["id"]),
                cesta=cesta,
                quantidade=produto['quantidade']
            )
            produto_cesta.save()
            cesta.produtoscesta_set.add(produto_cesta)
            cesta.save()

        return cesta

    def to_representation(self, instance):
        produtos_cesta = ProdutosCesta.objects.filter(cesta__id=instance.id)
        produtos_representation = []

        try:
            for produto_cesta in produtos_cesta:
                produto = produto_cesta.produto
                produtos_representation.append({
                    'id': produto.id,
                    'id_relacionamento_produto_cesta': produto_cesta.id,
                    'preco_unidade': produto.preco_unidade,
                    'preco_litro': produto.preco_litro,
                    'quantidade': produto_cesta.quantidade,
                    'ultima_atualizacao': produto.ultima_atualizacao,
                    'bebida': {
                        'id': produto.bebida.id,
                        'marca': {
                            'id': produto.bebida.marca.id,
                            'nome': produto.bebida.marca.nome
                        },
                        'modelo': {
                            'id': produto.bebida.modelo.id,
                            'descricao': produto.bebida.modelo.nome,
                            'volume': produto.bebida.modelo.volume
                        }
                    },
                    'loja': {
                        'id': produto.loja.id,
                        'nome': produto.loja.nome
                    }
                })

            return {
                'id': instance.id,
                'descricao': instance.descricao,
                'total': instance.total,
                'litros': instance.litros,
                'produtos': produtos_representation
            }
        except:
            return {
                'id': instance.id,
                'descricao': instance.descricao,
                'total': instance.total,
                'litros': instance.litros,
                'produtos': []
            }

class ProdutosCestaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProdutosCesta