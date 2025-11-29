class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_disponiveis(self):
        print("\nLivros disponíveis:")
        for livro in self.livros:
            if livro.disponivel:
                print(f"- {livro.titulo} ({livro.autor})")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print("Livro não encontrado.")
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro '{self.titulo}' emprestado com sucesso!")
        else:
            print(f"Livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        self.disponivel = True
        print(f"Livro '{self.titulo}' devolvido!")
# --- Testando o sistema de biblioteca ---
l1 = Livro("O Hobbit", "Tolkien")
l2 = Livro("1984", "George Orwell")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(l1)
biblioteca.adicionar_livro(l2)

biblioteca.listar_disponiveis()

biblioteca.emprestar_livro("O Hobbit")
biblioteca.emprestar_livro("O Hobbit")  # deve falhar

biblioteca.listar_disponiveis()
