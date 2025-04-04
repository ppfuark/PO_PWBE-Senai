class LojaVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = {}  
        self.carrinho = {}  
        self.desconto = 0.0
        self.total = 0.0

    def cadastrar_produto(self, id_produto, nome, preco, quantidade):
        if id_produto in self.estoque:
            print(f"O produto '{nome}' já está cadastrado.")
        else:
            self.estoque[id_produto] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
            print(f"Produto '{nome}' cadastrado com sucesso!")

    def adicionar_carrinho(self, id_produto, quantidade):
        if id_produto not in self.estoque:
            print(f"O produto não foi encontrado.")
        elif self.estoque[id_produto]['quantidade'] < quantidade:
            print(f"Estoque insuficiente para o produto.")
        else:
            self.carrinho[id_produto] = self.carrinho.get(id_produto, 0) + quantidade
            self.estoque[id_produto]['quantidade'] -= quantidade
            print(f"Produto '{self.estoque[id_produto]['nome']}' adicionado ao carrinho.")

    def conta_total(self):
        for i in self.carrinho:
            product_price = self.estoque[i]['preco']
            product_qnt   = self.carrinho[i]
            self.total += (product_price*product_qnt) 
        print(f"Total: {self.total}")

    def desconto(self, desconto):
        if desconto < 0 or desconto > 100:
            print("Desconto inválido!")
        else:
            pass


loja = LojaVirtual('Sim')

loja.cadastrar_produto(1, "batata", 12, 20)
loja.adicionar_carrinho(1, 15)

loja.conta_total()