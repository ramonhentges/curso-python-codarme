from django.db import models

# Create your models here.


class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link


aula_js = Evento("aula JS", "Frontend", "Casa do Zé")
aula_python = Evento("aula Python", "Backend", link="tamarcado.com")

eventos = [aula_js, aula_python]
