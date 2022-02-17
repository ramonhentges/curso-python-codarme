def inverte_lista(lista):
    inverted = []
    for value in lista:
        inverted.insert(0, value)
    return inverted


lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
