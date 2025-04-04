class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, titulo, qnt):
        self.livros[titulo] = qnt
        print(f"Livro '{titulo}' cadastrado - {qnt}.")

    def fazer_emprestimo(self, titulo):
        if titulo in self.livros and self.livros[titulo] > 0:
            self.livros[titulo] -= 1
            print(f"Livro '{titulo}' emprestado.")
        else:
            print(f"Livro '{titulo}' não disponível.")

    def devolver_livro(self, titulo):
        if titulo in self.livros:
            self.livros[titulo] += 1
            print(f"Livro '{titulo}' devolvido.")
        else:
            print(f"Livro '{titulo}' não cadastrado.")

    def verificar_disponibilidade(self, titulo):
        if titulo in self.livros and self.livros[titulo] > 0:
            print(f"Livro '{titulo}' está disponível ({self.livros[titulo]}).")
        else:
            print(f"Livro '{titulo}' não disponível.")


