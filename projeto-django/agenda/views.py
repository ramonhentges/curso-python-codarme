from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from agenda.models import Categoria, Evento


# Create your views here.


def listar_eventos(request):
    hoje = date.today()
    eventos = Evento.objects.exclude(data__lt=hoje).order_by('data')
    return render(request=request, context={"eventos": eventos}, template_name="agenda/listar_eventos.html")


def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    #template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(
    #    context={"evento": evento}, request=request)
    # return HttpResponse(rendered_template)
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_evento.html")


def participar(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))


def listar_categorias(request):
    categorias = Categoria.objects.all()
    for categoria in categorias:
        eventos = Evento.objects.filter(categoria=categoria)
        qtd_eventos = eventos.count()
        categoria.qtd_eventos = qtd_eventos

    return render(request=request, context={"categorias": categorias}, template_name="agenda/listar_categorias.html")


def exibir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request=request, context={"categoria": categoria}, template_name="agenda/exibir_categoria.html")
