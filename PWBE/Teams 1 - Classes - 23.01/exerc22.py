class Produto:
    def __init__(self, nome, preco_compra, preco_venda, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print(f"Estoque insuficiente para {self.nome}.")

    def mostrar_detalhes(self):
        print(f"{self.nome}: {self.quantidade} unidades, Preço de compra: R$ {self.preco_compra:.2f}, Preço de venda: R$ {self.preco_venda:.2f}")


produto1 = Produto("Mouse", 20.0, 50.0, 100)
produto2 = Produto("Teclado", 50.0, 120.0, 50)

produto1.adicionar_estoque(10)
produto2.vender(5)

produto1.mostrar_detalhes()
produto2.mostrar_detalhes()
