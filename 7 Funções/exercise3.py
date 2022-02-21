def maior_idade(pessoa):
    nome, idade = pessoa
    maior_de_idade = idade >= 18
    if(maior_de_idade):
        print('A pessoa ' + nome + ' é maior de idade')
    else:
        print('A pessoa ' + nome + ' não é maior de idade')

maior_idade(('Ramon', 27))
