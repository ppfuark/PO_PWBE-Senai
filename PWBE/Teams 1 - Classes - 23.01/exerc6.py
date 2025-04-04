class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def disponibilidade(self):
        return self.quantidade > 0

produto = Produto("Short", 50.0, 10)
print(f"Valor total em estoque: R${produto.valor_total()}")
print("Disponível para venda?" , produto.disponibilidade())
