USUARIO = 'ramon'
SENHA = '1234567'

nome_usuario = input('Digite seu nome de usuário: ')
senha_usuario = input('Digite sua senha: ')

if nome_usuario == USUARIO and senha_usuario == SENHA:
    print('Autenticado com sucesso')
elif nome_usuario != USUARIO:
    print('O usuário informado não existe')
elif senha_usuario != SENHA:
    print('Senha incorreta')