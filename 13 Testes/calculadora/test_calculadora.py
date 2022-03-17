from calculadora import somar, dividir, multiplicar, subtrair
import unittest


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_por_zero_(self):
        self.assertEqual(dividir(10, 0), "Não é um número")

    def test_divide_numero_por_negativo(self):
        self.assertEqual(dividir(10, -2), -5)


class TestMultiplicar(unittest.TestCase):
    def test_multiplica_numero_por_1_retorna_o_numero(self):
        self.assertEqual(multiplicar(10, 1), 10)

    def test_multiplica_por_zero_(self):
        self.assertEqual(multiplicar(10, 0), 0)

    def test_multiplica_numero_por_negativo(self):
        self.assertEqual(multiplicar(10, -2), -20)

    def test_multiplica_dois_negativos(self):
        self.assertEqual(multiplicar(-5, -7), 35)


class TestSubtrair(unittest.TestCase):
    def test_subtracao_de_dois_numeros_inteiros(self):
        self.assertEqual(subtrair(2, 4), -2)

    def test_subtracao_de_numero_com_zero(self):
        self.assertEqual(subtrair(2, 0), 2)

    def test_subtracao_de_dois_negativos(self):
        self.assertEqual(subtrair(-6, -9), 3)


unittest.main()
