from django.http import HttpResponse
from django.shortcuts import render

from agenda.models import eventos
# Create your views here.


def index(request):
    return HttpResponse("Olá Mundo")


def exibir_evento(request):
    evento = eventos[0]
    return HttpResponse(f"""
    <html>
    <body>
        <h1>{evento.nome}</h1>
        <p>Local: {evento.local}</p>
        <p>Categoria: {evento.categoria}</p>
    </body>
    """)
