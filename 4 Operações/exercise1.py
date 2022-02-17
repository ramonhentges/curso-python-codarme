number = input('Escolha um número: ')

number = int(number)

isEven = number % 2 == 0

if(isEven):
    print('O número', number, 'é par')
else:
    print('O número', number, 'é ímpar')