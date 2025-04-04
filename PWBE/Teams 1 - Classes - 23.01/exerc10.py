class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return "Livro emprestado!"
        return "Livro não disponível."

    def devolver(self):
        self.disponivel = True
        return "Livro devolvido!"

    def disponibilidade(self):
        return "Disponível" if self.disponivel else "Indisponível"

livro = Livro("O Senhor dos Anéis", "Sim", 1216)
print(livro.emprestar())
print(livro.disponibilidade())
print(livro.devolver())
print(livro.disponibilidade())
