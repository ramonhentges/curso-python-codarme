from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import Evento


# Create your views here.


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request=request, context={"eventos": eventos}, template_name="agenda/listar_eventos.html")


def exibir_evento(request):
    evento = {
        "nome": "teste",
        "categoria": "A",
        "local": "Rio de Janeiro"
    }
    #template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(
    #    context={"evento": evento}, request=request)
    # return HttpResponse(rendered_template)
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_evento.html")
