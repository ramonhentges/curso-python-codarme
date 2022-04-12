from calendar import month
from datetime import date, datetime, timedelta, timezone
import json
from urllib import response
from rest_framework.test import APITestCase

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


class TestListagemAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(data_horario=datetime(2022, 3, 15
                                                         ), nome_cliente="Ramon", email_cliente="cied@ts.co.po", telefone_cliente="+5599986308495")

        agendamento_serializado = {
            "id": 1,
            "data_horario": "2022-03-15T00:00:00Z",
            "nome_cliente": "Ramon",
            "email_cliente": "cied@ts.co.po",
            "telefone_cliente": "+5599986308495"
        }
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], agendamento_serializado)


class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        data = date.today()
        dias_para_adicionar = 1
        # valida se o dia é um sábado ou domingo e adiciona 2 dias
        if data.weekday() > 4:
            dias_para_adicionar = 2

        data_horario = datetime(
            year=data.year, day=data.day, month=data.month, hour=10, minute=0, second=0, tzinfo=timezone.utc) + timedelta(days=dias_para_adicionar)
        email_cliente = "cied@ts.co.po"
        nome_cliente = "Ramon"
        telefone_cliente = "+5599986308495"

        request_data = {
            "data_horario": data_horario,
            "nome_cliente": nome_cliente,
            "email_cliente": email_cliente,
            "telefone_cliente": telefone_cliente
        }

        response = self.client.post(
            "/api/agendamentos/", request_data, format="json")
        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(agendamento_criado.data_horario, data_horario)
        self.assertEqual(agendamento_criado.nome_cliente, nome_cliente)
        self.assertEqual(agendamento_criado.email_cliente, email_cliente)
        self.assertEqual(agendamento_criado.telefone_cliente, telefone_cliente)
        self.assertEqual(response.status_code, 201)

    def test_data_no_passado_erro_400(self):
        data = date.today()
        data_horario = datetime(
            year=data.year, day=data.day, month=data.month, hour=10, minute=0, second=0, tzinfo=timezone.utc) - timedelta(days=1)
        request_data = {
            "data_horario": data_horario,
            "nome_cliente": "Ramon",
            "email_cliente": "cied@ts.co.po",
            "telefone_cliente": "+5599986308495"
        }

        response = self.client.post(
            "/api/agendamentos/", request_data, format="json")
        self.assertEqual(response.status_code, 400)
