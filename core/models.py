from __future__ import unicode_literals

from django.db import models

# Create your models here.
class pessoa (models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=50)
    status = models.BooleanField()


    def __str__(self):
        return str(self.nome)

