# --- Sistema com POO ---

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        self.quantidade += qtd

    def remover(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
        else:
            print("Estoque insuficiente!")

    def valor_total(self):
        return self.quantidade * self.preco


# Testando o sistema orientado a objetos
p = Produto("Camisa", 10, 50.0)

p.adicionar(5)
p.remover(3)

print("Valor total em estoque:", p.valor_total())
print(f"{p.nome} - {p.quantidade} unidades - R$ {p.preco}")
