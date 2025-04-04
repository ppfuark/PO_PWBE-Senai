class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = {}

    def cliente(self, nome):
        self.clientes.append(nome)
        print(f"Cliente {nome} cadastrado.")

    def abrir_conta(self, nome, saldo=0):
        if nome not in self.clientes:
            print("Cliente não cadastrado.")
            return
        self.contas[nome] = saldo
        print(f"Conta aberta para {nome} com saldo inicial de R${saldo}")

    def saque(self, nome, valor):
        if nome not in self.contas or self.contas[nome] < valor:
            print("Saque não autorizado.")
            return
        self.contas[nome] -= valor
        print(f"Saque de R${valor} realizado com sucesso.")

    def deposito(self, nome, valor):
        if nome not in self.contas:
            print("Cliente não possui conta.")
            return
        self.contas[nome] += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def transferencia(self, origem, destino, valor):
        if origem not in self.contas or destino not in self.contas:
            print("Transferência não autorizada.")
            return
        if self.contas[origem] < valor:
            print("Saldo insuficiente para transferência.")
            return
        self.contas[origem] -= valor
        self.contas[destino] += valor
        print(f"Transferência de R${valor} realizada com sucesso.")

banco = Banco()
banco.cliente("João")
banco.abrir_conta("João", 500)
banco.deposito("João", 200)
banco.saque("João", 100)
banco.transferencia("João", "Maria", 50)