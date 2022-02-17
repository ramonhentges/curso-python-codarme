print('Listagem de números inteiros positivos!\nPara parar, digite um número negativo')

numbers = []

last_number = 0

while last_number >= 0:
    last_number = int(input('Insira um número: '))
    if last_number >= 0:
        numbers.append(last_number)

print(numbers)
