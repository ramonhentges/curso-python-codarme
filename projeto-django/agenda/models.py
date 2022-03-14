from tkinter import CASCADE
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"
    # def __init__(self, nome, categoria, local=None, link=None):
    #    self.nome = nome
    #    self.categoria = categoria
    #    self.local = local
    #    self.link = link
