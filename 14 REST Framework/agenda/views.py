from datetime import datetime, timedelta, timezone
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import AnonymousUser, User
from agenda.libs.brasil_api import is_feriado
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer, PrestadorSerializer
from agenda.utils import entre_horario_trabalho, entre_intervalo


# Create your views here.


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        #username = request.query_params.get("username", None)
        print(request.user.username)
        if not isinstance(request.user, AnonymousUser):
            return True
        return False


class IsPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False


class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsPrestador]
    queryset = Agendamento.objects.exclude(cancelado=True)
    serializer_class = AgendamentoSerializer


""" @api_view(http_method_names=["GET", "PATCH", "DELETE"])
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
"""


class AgendamentoList(generics.ListCreateAPIView):

    serializer_class = AgendamentoSerializer
    permission_classes = [IsOwnerOrCreateOnly]

    def get_queryset(self):
        # username = self.request.query_params.get("username", None)
        username = self.request.user.username
        queryset = Agendamento.objects.filter(
            prestador__username=username).exclude(cancelado=True)
        return queryset


class PrestadorList(generics.ListAPIView):

    permission_classes = [permissions.IsAdminUser]
    serializer_class = PrestadorSerializer
    queryset = User.objects.all()


""" @api_view(http_method_names=["GET", "POST"])
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
 """


@api_view(http_method_names=["GET"])
def horarios_list(request):
    if request.method == "GET":
        data_query = request.query_params.get("data")
        prestador = request.query_params.get("prestador")
        if prestador == None:
            return JsonResponse({"username": "Username não informado"}, status=400)
        data = datetime.fromisoformat(data_query).date()
        dt_com_timezone = datetime(
            data.year, data.month, data.day, tzinfo=timezone.utc)

        try:
            if is_feriado(dt_com_timezone):
                return JsonResponse([], safe=False)
        except ValueError:
            ...

        if dt_com_timezone.weekday() == 6:
            return JsonResponse([], safe=False)

        horarios_agendados = list(Agendamento.objects.filter(
            data_horario__date=dt_com_timezone).filter(cancelado=False).filter(prestador__username=prestador).order_by('data_horario'))
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
