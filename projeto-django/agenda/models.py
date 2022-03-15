from tkinter import CASCADE
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

    @classmethod
    def cria_categoria(cls, nome):
        if nome == '' or nome == None:
            raise ValueError(
                "Categoria deve possuir um nome e não pode ser em branco.")
        categoria = Categoria(nome=nome)
        categoria.save()
        return categoria


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

    @classmethod
    def cria_evento(cls, nome, categoria, local='', link='', data=None):
        if not local == '' and not link == '':
            raise ValueError("Evento não pode possuir local e link.")
        evento = Evento(nome=nome, categoria=categoria,
                        local=local, link=link, data=data)
        evento.save()
        return evento
    # def __init__(self, nome, categoria, local=None, link=None):
    #    self.nome = nome
    #    self.categoria = categoria
    #    self.local = local
    #    self.link = link
