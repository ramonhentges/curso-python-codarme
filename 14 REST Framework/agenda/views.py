from datetime import datetime, timezone, timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from agenda.models import Agendamento, entre_horario_trabalho, entre_intervalo
from agenda.serializers import AgendamentoSerializer

# Create your views here.


@api_view(http_method_names=["GET", "PATCH", "DELETE"])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id, cancelado=False)
    if request.method == "GET":
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)

    if request.method == "PATCH":
        serializer = AgendamentoSerializer(
            obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        obj.cancelado = True
        obj.save()
        return Response(status=204)


@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method == "GET":
        qs = Agendamento.objects.exclude(cancelado=True)
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(http_method_names=["GET"])
def horarios_list(request):
    if request.method == "GET":
        data_query = request.query_params.get("data")
        data = datetime.fromisoformat(data_query).date()
        dt_com_timezone = datetime(
            data.year, data.month, data.day, tzinfo=timezone.utc)
        if dt_com_timezone.weekday() == 6:
            return JsonResponse([], safe=False)

        horarios_agendados = list(Agendamento.objects.filter(
            data_horario__date=dt_com_timezone).filter(cancelado=False).order_by('data_horario'))
        data_hora_inicial = datetime(
            data.year, data.month, data.day,  hour=9, minute=0, second=0, tzinfo=timezone.utc)
        horarios_disponiveis = []
        horario_verificacao = data_hora_inicial
        if dt_com_timezone.weekday() == 5:
            data_hora_ultimo_atendimento = datetime(
                data.year, data.month, data.day,  hour=12, minute=30, second=0, tzinfo=timezone.utc)
        else:
            data_hora_ultimo_atendimento = datetime(
                data.year, data.month, data.day,  hour=17, minute=30, second=0, tzinfo=timezone.utc)

        while horario_verificacao <= data_hora_ultimo_atendimento:
            if entre_horario_trabalho(horario_verificacao, dt_com_timezone) and ((len(horarios_agendados) > 0 and horario_verificacao <= horarios_agendados[0].data_horario - timedelta(minutes=30)) or len(horarios_agendados) == 0):
                horarios_disponiveis.append(horario_verificacao.isoformat())
            elif len(horarios_agendados) > 0 and horario_verificacao > horarios_agendados[0].data_horario - timedelta(minutes=30):
                horario_verificacao = horarios_agendados[0].data_horario
                horarios_agendados.pop(0)
            if dt_com_timezone.weekday() != 5 and entre_intervalo(horario_verificacao, dt_com_timezone):
                horario_verificacao = datetime(
                    data.year, data.month, data.day,  hour=13, minute=0, second=0, tzinfo=timezone.utc)
            else:
                horario_verificacao = horario_verificacao + \
                    timedelta(minutes=30)

        return JsonResponse(horarios_disponiveis, safe=False)
