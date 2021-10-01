from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)