print('Média de números inteiros positivos!\nPara parar, digite um número negativo')
numbers = []

last_number = 0

while last_number >= 0:
    last_number = int(input('Insira um número: '))
    if last_number >= 0:
        numbers.append(last_number)

sum = 0

for value in numbers:
    sum += value

average = sum // len(numbers)

print('A média é:', average)
