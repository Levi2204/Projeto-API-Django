from django.db import models


class ObjetoPerdido(models.Model):
    id_objeto = models.AutoField(primary_key=True)
    nome_objeto = models.CharField(max_length=255)
    cor = models.CharField(max_length=100)
    data_perdido = models.CharField(max_length=50)

    objects = models.Manager()

    class Meta:
        db_table = "objetos_perdidos"

    def __str__(self):
        return self.nome_objeto


class ObjetoAchado(models.Model):
    id_objetoA = models.AutoField(primary_key=True)
    nome_objeto_achado = models.CharField(max_length=255)
    cor_achado = models.CharField(max_length=100)
    nome_pessoa = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    contato = models.CharField(max_length=200)

    objects = models.Manager()

    class Meta:
        db_table = "objetos_achados"

    def __str__(self):
        return self.nome_objeto_achado
