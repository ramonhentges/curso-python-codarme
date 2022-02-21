import hashlib


def hash_string(texto):
    """
    Recebe um texto como string e retorna a representação hash desse texto.
    Exemplo:
        hash_string("123") -> "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    """
    return hashlib.sha256(texto.encode()).hexdigest()


class Usuario:
    id = 0

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = Usuario.id
        Usuario.id += 1

    def get_hash_password(self):
        return hash_string(self.senha)

    def get_hash_for_html(self):
        hash = self.get_hash_password()
        return f'{hash[0:5]}...'
