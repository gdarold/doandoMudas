from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from apps.endereco.models import Endereco
from apps.pessoa.models import Pessoa
from apps.tipo_doacao.models import Tipo_doacao
from apps.tipo_planta.models import Tipo_planta


class Doacao(models.Model):
    doador = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)

    tipo_doacao = models.ForeignKey(Tipo_doacao, on_delete=models.CASCADE)
    tipo_planta = models.ForeignKey(Tipo_planta, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    peso = models.DecimalField(max_digits=4, decimal_places=2,default=0.1)
    custo = models.DecimalField(max_digits=4, decimal_places=2, default=1)
    status = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('list_doacoes')

    def __str__(self):
        return self.descricao

