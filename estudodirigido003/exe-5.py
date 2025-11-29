class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.itens = []  # inventário do jogador

    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"{self.nome} recebeu R${valor}. Novo saldo: R${self.saldo}")
        else:
            print("Valor inválido!")

    def comprar_item(self, item, preco):
        if preco <= self.saldo:
            self.saldo -= preco
            self.itens.append(item)
            print(f"{self.nome} comprou {item}! Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente para comprar este item.")
j1 = Jogador("Charles")

j1.adicionar_saldo(100)
j1.comprar_item("Espada", 50)
j1.comprar_item("Armadura", 80)  # Deve falhar

print("Itens do Charles:", j1.itens)

