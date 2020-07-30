from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Endereco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)

