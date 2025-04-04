class MaquinaDeVendas:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = {} 
        self.total = 0.0  
        self.dinheiro_inserido = 0.0  

    def cadastrar_produto(self, id_produto, nome, preco, quantidade):
        if id_produto in self.estoque:
            print(f"O produto '{nome}' já está cadastrado.")
        else:
            self.estoque[id_produto] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
            print(f"Produto '{nome}' cadastrado com sucesso!")

    def exibir_produtos(self):
        print("\nProdutos Disponíveis:")
        for id_produto, detalhes in self.estoque.items():
            nome = detalhes['nome']
            preco = detalhes['preco']
            quantidade = detalhes['quantidade']
            print(f"ID: {id_produto} | Nome: {nome} | Preço: R${preco:.2f} | Quantidade: {quantidade}")

    def selecionar_produto(self, id_produto, quantidade):
        if id_produto not in self.estoque:
            print("Produto não encontrado.")
        elif self.estoque[id_produto]['quantidade'] < quantidade:
            print("Estoque insuficiente para este produto.")
        else:
            self.total += self.estoque[id_produto]['preco'] * quantidade
            self.estoque[id_produto]['quantidade'] -= quantidade
            print(f"{quantidade}x '{self.estoque[id_produto]['nome']}' selecionado(s).")

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            print("Insira um valor válido.")
        else:
            self.dinheiro_inserido += valor
            print(f"Dinheiro inserido: R${valor:.2f}")

    def finalizar_compra(self):
        if self.dinheiro_inserido < self.total:
            print(f"Dinheiro insuficiente. Faltam R${self.total - self.dinheiro_inserido:.2f}.")
        else:
            troco = self.dinheiro_inserido - self.total
            print(f"Compra finalizada! Troco: R${troco:.2f}.")
            self.dinheiro_inserido = 0.0
            self.total = 0.0

    def exibir_estoque(self):
        print("\nEstoque Atualizado:")
        for id_produto, detalhes in self.estoque.items():
            nome = detalhes['nome']
            quantidade = detalhes['quantidade']
            print(f"ID: {id_produto} | Nome: {nome} | Quantidade: {quantidade}")


maquina = MaquinaDeVendas("Loja Virtual")
maquina.cadastrar_produto(1, "Chocolate", 5.00, 20)
maquina.cadastrar_produto(2, "Refrigerante", 7.00, 15)
maquina.cadastrar_produto(3, "Batata", 4.00, 30)

maquina.exibir_produtos()
maquina.selecionar_produto(2, 2)
maquina.selecionar_produto(1, 3)
maquina.inserir_dinheiro(20.00)
maquina.finalizar_compra()
maquina.exibir_estoque()
