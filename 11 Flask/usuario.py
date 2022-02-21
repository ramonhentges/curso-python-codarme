class Usuario:
    quantidade = 0
    id = 0

    def __init__(self, nome, email):
        self.id = Usuario.id
        self.nome = nome
        self.email = email
        self.tipo = 'Usuário'
        Usuario.quantidade += 1
        Usuario.id += 1

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")
