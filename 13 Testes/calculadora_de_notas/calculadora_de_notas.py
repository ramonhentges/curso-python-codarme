from aluno import Aluno
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


class Calculadora:
    def __init__(self, alunos: list[Aluno], media: int):
        self.alunos = alunos
        self.media = media

    def get_media(self):
        soma = 0
        for aluno in self.alunos:
            soma += aluno.nota
        media = soma / len(self.alunos)
        return media

    def get_maior_nota(self):
        maior = 0
        for aluno in self.alunos:
            if aluno.nota > maior:
                maior = aluno.nota
        return maior

    def get_menor_nota(self):
        menor = 10
        for aluno in self.alunos:
            if aluno.nota < menor:
                menor = aluno.nota
        return menor

    def get_aprovados(self):
        aprovados = []
        for aluno in self.alunos:
            if aluno.nota >= self.media:
                aprovados.append(aluno)
        return aprovados

    def get_reprovados(self):
        reprovados = []
        for aluno in self.alunos:
            if aluno.nota < self.media:
                reprovados.append(aluno)
        return reprovados

    def get_letras(self):
        letras = []
        for aluno in self.alunos:
            if aluno.nota == 10:
                letras.append("A+")
            elif aluno.nota >= 9:
                letras.append("A")
            elif aluno.nota >= 7:
                letras.append("B")
            elif aluno.nota >= 5:
                letras.append("C")
            elif aluno.nota >= 3:
                letras.append("D")
            elif aluno.nota >= 1:
                letras.append("E")
            elif aluno.nota >= 0:
                letras.append("F")
        return letras
