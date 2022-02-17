print('Saiba a soma de todos os números até o informado!')

choosed_number = int(input('Digite um valor inteiro positivo: '))

if choosed_number < 0:
    print('Número inválido, insira um valor inteiro positivo')
else:
    actual = 1
    sum = 0
    while actual <= choosed_number:
        sum = sum + actual
        actual += 1

    print('A soma de todos os números é:', sum)
