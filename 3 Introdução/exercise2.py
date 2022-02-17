valor_compras = 108.12
desconto = 0.15
quantidade_itens = 3
percentual_sobre_compra = 1 - desconto
valor_final = valor_compras * percentual_sobre_compra
valor_item = valor_final / quantidade_itens

print("O valor final das compras é:", valor_final)
print("O custo médio de cada item é:", valor_item)