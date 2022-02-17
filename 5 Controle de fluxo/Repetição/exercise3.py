print('Saiba se o número informado é primo!')

choosed_number = int(input('Digite o número: '))

calc_number = choosed_number

if choosed_number < 0:
    calc_number = calc_number * -1

divider = 2
isPrime = True

while divider < calc_number:
    if calc_number % divider == 0:
        isPrime = False
        break
    divider+=1

if isPrime:
    print('O número informado é primo')
else:
    print('O número informado não é primo')