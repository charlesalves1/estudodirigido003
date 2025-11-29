class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario:.2f}")
f1 = Funcionario("Charles", "Programador Júnior", 3000)
f1.aumentar_salario(10)

f2 = Funcionario("Maria", "Gerente", 8000)
f2.aumentar_salario(20)
