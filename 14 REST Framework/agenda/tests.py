from datetime import datetime, timezone
import json
from rest_framework.test import APITestCase

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


class TestListagemAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(data_horario=datetime.now(tz=timezone.utc
                                                             ), nome_cliente="Ramon", email_cliente="cied@ts.co.po", telefone_cliente="+5599986308495")
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
