class Usuario:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def adicionar_saldo(self, valor):
        self.saldo += valor
class Pagamento:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor
        self.status = "pendente"

    def processar(self):
        if self.status == "pendente":
            self.usuario.adicionar_saldo(self.valor)
            self.status = "aprovado"
            print(f"Pagamento de R${self.valor} para {self.usuario.nome} foi aprovado!")
        else:
            print("Este pagamento já foi processado.")
u1 = Usuario("Charles", saldo=50)

pag1 = Pagamento(u1, 100)
pag1.processar()     # adiciona saldo ao usuário
pag1.processar()     # não deve processar novamente

print("Saldo final do usuário:", u1.saldo)
print("Status do pagamento:", pag1.status)
