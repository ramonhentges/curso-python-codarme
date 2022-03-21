import unittest
from aluno import Aluno
from calculadora_de_notas import Calculadora


class TestMediaNotas(unittest.TestCase):
    def retorna_media_de_tres_alunos(self):
        aluno1 = Aluno("Ramon", 9)
        aluno2 = Aluno("Jose", 7)
        aluno3 = Aluno("Fernanda", 8)
        alunos = [aluno1, aluno2, aluno3]
        calculadora = Calculadora([alunos])
        self.assertEqual(calculadora.get_media(), 8)


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
