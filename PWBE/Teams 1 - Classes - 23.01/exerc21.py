class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico_compras = []

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.carrinho = []
        self.total = 0

    def adicionar_produto(self, produto):
        self.carrinho.append(produto)
        self.total += produto.preco

    def calcular_frete(self):
        return 10 if self.total < 100 else 0

    def aplicar_desconto(self, percentual):
        self.total -= self.total * (percentual / 100)

    def finalizar_pedido(self):
        self.cliente.historico_compras.extend(self.carrinho)
        self.carrinho.clear()


cliente1 = Cliente("João")
produto1 = Produto("Camiseta", 50)
pedido = Pedido(cliente1)
pedido.adicionar_produto(produto1)

frete = pedido.calcular_frete()
print(f"Frete: R$ {frete:.2f}")

pedido.aplicar_desconto(10)
print(f"Total com desconto: R$ {pedido.total:.2f}")

pedido.finalizar_pedido()
