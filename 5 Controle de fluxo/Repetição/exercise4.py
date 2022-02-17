NUMBER_TO_DISCOVER = 6
MAX_ATTEMPTS = 3
print('Adivinhe o número escondido!')

attempt = 1

while attempt <= MAX_ATTEMPTS:
    choosed = int(input('Escolha um número: '))
    if choosed == NUMBER_TO_DISCOVER:
        print('Parabéns, você acertou, o número escondido é o', NUMBER_TO_DISCOVER)
        break
    elif NUMBER_TO_DISCOVER < choosed:
        print('O número escondido é menor que o informado')
    elif NUMBER_TO_DISCOVER > choosed:
        print('O número escondido é maior que o informado')
    if attempt == MAX_ATTEMPTS:
        print('Você perdeu, o número escondido é o', NUMBER_TO_DISCOVER)
    attempt += 1