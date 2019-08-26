from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=11, unique=True)
    ativo = models.BooleanField()


    def __str__(self):
        return str(self.nome)


class TipoEquipamento (models.Model):
    descricao = models.CharField(max_length=100)


    def __str__(self):
        return str(self.descricao)


class Marca (models.Model):
    descricao = models.CharField(max_length=100)


    def __str__(self):
        return str(self.descricao)


class Modelo (models.Model):
    descricao = models.CharField(max_length=100)
    observacao = models.CharField(max_length=100)
    idMarca = models.ForeignKey(Marca, on_delete = models.PROTECT)


    def __str__(self):
        return str(self.descricao+' / '+str(self.idMarca))


class Equipamento (models.Model):
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField()
    idTipoEquipamento = models.ForeignKey(TipoEquipamento, on_delete = models.PROTECT)
    idModelo = models.ForeignKey(Modelo, on_delete = models.PROTECT)


class Armario (models.Model):
    descricao = models.CharField(max_length=45)
    idEquipamento = models.ForeignKey(Equipamento, on_delete = models.PROTECT)


class Reserva (models.Model):
    dataHoraInicial = models.DateTimeField(max_length=45)
    dataHoraFinal = models.DateTimeField(max_length=45)
    ativo = models.BooleanField()
    idArmario = models.ForeignKey(Armario, on_delete = models.PROTECT)
    idPessoa = models.ForeignKey(Pessoa, on_delete = models.PROTECT)


class Emprestimo (models.Model):
    dataHoraEmprestismo = models.DateTimeField(max_length=45)
    dataHoraDevolucao = models.DateTimeField(max_length=45)
    previsaoDevolucao = models.DateTimeField(max_length=45)
    idPessoa = models.ForeignKey(Pessoa, on_delete = models.PROTECT)


class EquipamentosEmprestimo (models.Model):
    emprestado = models.BooleanField(max_length=45)
    idEquipamento = models.ForeignKey(Equipamento, on_delete = models.PROTECT)
    idEmprestimo = models.ForeignKey(Emprestimo, on_delete = models.PROTECT)