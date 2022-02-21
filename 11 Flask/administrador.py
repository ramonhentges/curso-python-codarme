from usuario import Usuario


class Administrador(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.tipo = 'Administrador'

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email}) - Administrador")
