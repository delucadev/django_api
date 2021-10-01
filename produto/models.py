from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    quantidade_estoque = models.IntegerField()
    ativo = models.BooleanField()
