valor_compra = float(input('Valor de compra: '))
valor_frete = float(input('Valor do frete: '))
fidelizado = input('Fidelizado ("s" sim, "n" não): ')

valor_total = valor_compra + valor_frete

pode_usar_cupom = valor_total > 100 or fidelizado == 's'

print('O cupom pode ser utilizado?', pode_usar_cupom)