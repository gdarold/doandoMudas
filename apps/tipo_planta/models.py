from django.db import models

# Create your models here.


class Tipo_planta(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao
