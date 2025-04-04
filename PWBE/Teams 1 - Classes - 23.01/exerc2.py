class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Saldo atual: R${self.saldo:.2f}"
        else:
            return "O valor do depósito deve ser positivo."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente para realizar o saque."
        elif valor > 0:
            self.saldo -= valor
            return f"Saldo atual: R${self.saldo:.2f}"

conta = ContaBancaria(123456, "Paulo Henrique", 0)

print(conta.depositar(11111111))
print(conta.sacar(11111110))
