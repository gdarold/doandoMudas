from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from apps.endereco.models import Endereco


class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=12, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    celular = models.CharField(max_length=20)
    data = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('list_endereco')

    def __str__(self):
        return self.nome +' '+self.sobrenome


