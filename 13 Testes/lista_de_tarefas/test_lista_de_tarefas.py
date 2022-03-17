import unittest

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas
from datetime import datetime, timedelta


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        tarefa_concluida = Tarefa("Tarefa Teste 3")
        tarefa_concluida.concluir()
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_concluida)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_um,
            tarefa_dois,
        ])

    def test_retorna_lista_de_tarefas_com_concluidas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        tarefa_concluida = Tarefa("Tarefa Teste 3")
        tarefa_concluida.concluir()
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_concluida)

        self.assertEqual(lista.get_tarefas(incluir_concluidas=True), [
            tarefa_um,
            tarefa_dois,
            tarefa_concluida,
        ])


class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_atrasadas(self):
        agora = datetime.now()
        futuro = agora + timedelta(days=30)
        passado = agora - timedelta(days=30)

        tarefa_atrasada = Tarefa("Tarefa Teste 1", data_notificacao=passado)
        tarefa_nao_atrasada = Tarefa("Tarefa Teste 2", data_notificacao=futuro)
        tarefa_concluida_passada = Tarefa(
            "Tarefa Teste 3", data_notificacao=passado)
        tarefa_concluida_passada.concluir()
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_atrasada)
        lista.adicionar_tarefa(tarefa_nao_atrasada)
        lista.adicionar_tarefa(tarefa_concluida_passada)

        self.assertEqual(lista.get_tarefas_atrasadas(), [
            tarefa_atrasada,
        ])


class TestGetTarefasParaHoje(unittest.TestCase):
    def test_retorna_lista_de_tarefas_para_hoje(self):
        agora = datetime.now()
        futuro = agora + timedelta(days=30)
        passado = agora - timedelta(days=30)

        tarefa_no_passado = Tarefa("Tarefa Teste 1", data_notificacao=passado)
        tarefa_hoje = Tarefa("Tarefa Teste 2", data_notificacao=agora)
        tarefa_concluida_hoje = Tarefa(
            "Tarefa Teste 3", data_notificacao=agora)
        tarefa_concluida_hoje.concluir()
        tarefa_futura = Tarefa("Tarefa Teste 4", data_notificacao=futuro)

        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_no_passado)
        lista.adicionar_tarefa(tarefa_hoje)
        lista.adicionar_tarefa(tarefa_concluida_hoje)
        lista.adicionar_tarefa(tarefa_futura)

        self.assertEqual(lista.get_tarefas_para_hoje(), [
            tarefa_hoje,
            tarefa_concluida_hoje,
        ])


unittest.main()
