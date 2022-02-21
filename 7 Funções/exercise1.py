print('Saiba se o número informado é primo!')

def e_primo(number):
    calc_number = number

    if number < 0:
        calc_number = calc_number * -1

    divider = 2
    is_prime = True

    while divider < calc_number:
        if calc_number % divider == 0:
            is_prime = False
            break
        divider+=1
    return is_prime

choosed_number = int(input('Digite o número: '))
is_prime = e_primo(choosed_number)

print(is_prime)
