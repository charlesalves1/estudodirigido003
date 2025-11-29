class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def autenticar(self, email, senha):
        if self.email == email and self.senha == senha:
            return True
        return False


# --- Testes ---
u1 = Usuario("Charles", "charles@email.com", "1234")
u2 = Usuario("Maria", "maria@gmail.com", "abcd")

# Tentativas de login
print("Login Charles correto:", u1.autenticar("charles@email.com", "1234"))
print("Login Charles incorreto:", u1.autenticar("charles@email.com", "9999"))

print("Login Maria correto:", u2.autenticar("maria@gmail.com", "abcd"))
print("Login Maria email errado:", u2.autenticar("test@gmail.com", "abcd"))
