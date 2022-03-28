import unittest
from aluno import Aluno
from calculadora_de_notas import Calculadora


class TestMediaNotas(unittest.TestCase):
    def test_media_de_tres_alunos(self):
        aluno1 = Aluno("Ramon", 9)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_media(), 8)


class TestMaiorNota(unittest.TestCase):
    def test_maior_nota_dos_alunos(self):
        aluno1 = Aluno("Ramon", 9)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_maior_nota(), 9)


class TestMenorNota(unittest.TestCase):
    def test_menor_nota_dos_alunos(self):
        aluno1 = Aluno("Ramon", 9)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_menor_nota(), 7)


class TestAprovados(unittest.TestCase):
    def test_receber_aprovados_media_6(self):
        aluno1 = Aluno("Ramon", 3)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 6)
        aluno4 = Aluno("Jose", 5)
        aluno5 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_aprovados(), [aluno2, aluno3, aluno5])

    def test_receber_aprovados_media_5(self):
        aluno1 = Aluno("Ramon", 3)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 6)
        aluno4 = Aluno("Jose", 5)
        aluno5 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
        calculadora = Calculadora(alunos, 5)
        self.assertEqual(calculadora.get_aprovados(), [
                         aluno2, aluno3, aluno4, aluno5])


class TestRerovados(unittest.TestCase):
    def test_receber_reprovados_media_6(self):
        aluno1 = Aluno("Ramon", 3)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 6)
        aluno4 = Aluno("Jose", 5)
        aluno5 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_reprovados(), [aluno1, aluno4])

    def test_receber_reprovados_media_5(self):
        aluno1 = Aluno("Ramon", 3)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 6)
        aluno4 = Aluno("Jose", 5)
        aluno5 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
        calculadora = Calculadora(alunos, 5)
        self.assertEqual(calculadora.get_reprovados(), [aluno1])


class TestMenorNota(unittest.TestCase):
    def test_menor_nota_dos_alunos(self):
        aluno1 = Aluno("Ramon", 3)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 6)
        aluno4 = Aluno("Jose", 0)
        aluno5 = Aluno("Fernanda", 10)
        aluno6 = Aluno("Fernanda", 9)
        aluno7 = Aluno("Fernanda", 2)
        alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7]
        calculadora = Calculadora(alunos, 6)
        self.assertEqual(calculadora.get_letras(), [
                         "D", "B", "C", "F", "A+", "A", "E"])


unittest.main()

"""
CALCULADORA DE NOTAS
====================
1. Recebe uma turma, composta por uma lista de Alunos(nome, nota) e média para aprovar um aluno.
2. Calcula a média das notas da turma (get_media).
3. Qual a maior e menor nota (get_maior_nota, get_menor_nota).
4. Retorna alunos aprovados e reprovados (get_aprovados, get_reprovados).
5. Retorna lista de notas em representação de "letra".
    - nota == 10       =>    "A+"
    - 9 <= nota < 10   =>    "A"
    - 7 <= nota < 9    =>    "B"
    - 5 <= nota < 7    =>    "C"
    - 3 <= nota < 5    =>    "D"
    - 1 <= nota < 3    =>    "E"
    - 0 <= nota < 1    =>    "F
"""
