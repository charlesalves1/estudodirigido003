# --- Sistema sem POO ---

def adicionar_estoque(produto, qtd):
    produto["quantidade"] += qtd


def remover_estoque(produto, qtd):
    if qtd <= produto["quantidade"]:
        produto["quantidade"] -= qtd
    else:
        print("Estoque insuficiente!")


def valor_total(produto):
    return produto["quantidade"] * produto["preco"]


# Testando o sistema
produto = {
    "nome": "Camisa",
    "quantidade": 10,
    "preco": 50.0
}

adicionar_estoque(produto, 5)
remover_estoque(produto, 3)

print("Valor total em estoque:", valor_total(produto))
print(produto)
