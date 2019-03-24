from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=60, null=False)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=60, null=False)
    volume = models.IntegerField()
    
    def __str__(self):
        return "%s - %sml" % (self.nome, self.volume)

class Bebida(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, null=False, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.marca, self.modelo)

class Loja(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=60, null=False)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    bebida = models.ForeignKey(Bebida, null=False, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, null=False, on_delete=models.CASCADE)
    preco_unidade = models.FloatField(null=False)
    preco_litro = models.FloatField(null=False)
    ultima_atualizacao = models.DateField(null=False)
    
    def __str__(self):
        return "%s - %s" % (self.bebida,self.loja)

class Cesta(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(null=False)
    total = models.FloatField(null=False)
    litros = models.FloatField(null=False)
    produtos = models.ManyToManyField(Produto, through="ProdutosCesta", related_name="produtos", blank=True)

    def __str__(self):
        return self.descricao

class ProdutosCesta(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cesta = models.ForeignKey(Cesta, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)
    preco = models.FloatField(null=False)