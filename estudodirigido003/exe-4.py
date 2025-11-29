class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\nProdutos no pedido:")
        for p in self.produtos:
            print(f"- {p.nome} | R$ {p.preco:.2f}")

    def valor_total(self):
        total = sum(p.preco for p in self.produtos)
        return total


# --- Testando ---
p1 = Produto("Camisa", 50)
p2 = Produto("Tênis", 200)
p3 = Produto("Boné", 30)

pedido = Pedido()
pedido.adicionar_produto(p1)
pedido.adicionar_produto(p2)
pedido.adicionar_produto(p3)

pedido.listar_produtos()
print("\nValor total do pedido: R$", pedido.valor_total())
