from unittest import result


print('Faça um cálculo entre dois números!')

a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))
op = input('Insira o operador (+, -, *, /): ')

if op == '/' and b == 0:
    print('Não é possível realizar divisão por zero!')
else:
    result
    if op == '+':
        result = a + b
    if op == '-':
        result = a - b
    if op == '*':
        result = a * b
    if op == '/':
        result = a / b
    print('O resultado da operação é:', result)