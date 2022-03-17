import unittest
from datetime import datetime, timedelta
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        # year, month, day, hour, minute, second, millisecond
        dt_original = datetime(2022, 2, 10, 9, 10)
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(15)

        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)


class TestDescricao(unittest.TestCase):
    def test_adiciona_descricao(self):
        tarefa = Tarefa("Estudar Python")
        nova_descricao = "Conteúdo TOP"
        tarefa.adicionar_descricao(nova_descricao)
        self.assertEqual(tarefa.descricao, nova_descricao)


class TestAtrasada(unittest.TestCase):
    def test_tarefa_nao_atrasada_prazo_hoje(self):
        hoje = datetime.now()

        tarefa = Tarefa("Estudar Python", data_notificacao=hoje)

        self.assertEqual(tarefa.atrasada(), False)

    def test_tarefa_atrasada(self):
        hoje = datetime.now()
        passado = hoje - timedelta(days=30)

        tarefa = Tarefa("Estudar Python", data_notificacao=passado)

        self.assertEqual(tarefa.atrasada(), True)

    def test_tarefa_nao_atrasada(self):
        hoje = datetime.now()
        futuro = hoje + timedelta(days=30)

        tarefa = Tarefa("Estudar Python", data_notificacao=futuro)

        self.assertEqual(tarefa.atrasada(), False)

    def test_tarefa_nao_atrasada_concluida(self):
        hoje = datetime.now()
        passado = hoje - timedelta(days=30)

        tarefa = Tarefa("Estudar Python", data_notificacao=passado)
        tarefa.concluir()

        self.assertEqual(tarefa.atrasada(), False)


unittest.main()
