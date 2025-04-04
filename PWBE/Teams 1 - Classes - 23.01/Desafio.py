class Evento:
    def __init__(self, data, hora, local, descricao):
        self.data = data
        self.hora = hora
        self.local = local
        self.descricao = descricao
        self.tarefas = []
        self.fornecedores = []
        self.pagamentos = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.append(pagamento)

class Tarefa:
    def __init__(self, descricao, responsavel, prazo):
        self.descricao = descricao
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

class Fornecedor:
    def __init__(self, nome, tipo_servico):
        self.nome = nome
        self.tipo_servico = tipo_servico

class Pagamento:
    def __init__(self, valor_total, parcelas, vencimento):
        self.valor_total = valor_total
        self.parcelas = parcelas
        self.vencimento = vencimento

class Responsavel:
    def __init__(self, nome):
        self.nome = nome

class Convidado:
    def __init__(self, nome):
        self.nome = nome



evento = Evento("01/03/2025", "18:00", "Salão ABC", "Casamento")

responsavel1 = Responsavel("Ana")
tarefa1 = Tarefa("Alugar salão", responsavel1, "20/02/2025")
evento.adicionar_tarefa(tarefa1)

fornecedor1 = Fornecedor("Sim", "talvez")
evento.adicionar_fornecedor(fornecedor1)

pagamento1 = Pagamento(5000, 5, "01/02/2025")
evento.adicionar_pagamento(pagamento1)

tarefa1.concluir()

print(f"Evento: {evento.descricao} em {evento.local} às {evento.hora} no dia {evento.data}")
print("Tarefas:")
for tarefa in evento.tarefas:
    print(f"- {tarefa.descricao} (Status: {tarefa.status}, Responsável: {tarefa.responsavel.nome})")
print("Fornecedores:")
for fornecedor in evento.fornecedores:
    print(f"- {fornecedor.nome} ({fornecedor.tipo_servico})")
print("Pagamentos:")
for pagamento in evento.pagamentos:
    print(f"- R$ {pagamento.valor_total:.2f}, {pagamento.parcelas} parcelas, vencimento: {pagamento.vencimento}")
