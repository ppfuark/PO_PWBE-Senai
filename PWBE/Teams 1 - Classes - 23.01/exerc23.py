class Tarefa:
    def __init__(self, descricao, prioridade, vencimento, categoria):
        self.descricao = descricao
        self.prioridade = prioridade
        self.vencimento = vencimento
        self.categoria = categoria
        self.status = "Pendente"

    def editar(self, descricao=None, prioridade=None, vencimento=None, categoria=None, status=None):
        if descricao: self.descricao = descricao
        if prioridade: self.prioridade = prioridade
        if vencimento: self.vencimento = vencimento
        if categoria: self.categoria = categoria
        if status: self.status = status

    def __str__(self):
        return f"{self.descricao} | Prioridade: {self.prioridade} | Vence em: {self.vencimento} | Categoria: {self.categoria} | Status: {self.status}"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self, descricao, prioridade, vencimento, categoria):
        nova_tarefa = Tarefa(descricao, prioridade, vencimento, categoria)
        self.tarefas.append(nova_tarefa)
        print("Tarefa criada com sucesso.")

    def listar_tarefas(self, filtro=None):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        
        for tarefa in self.tarefas:
            if filtro:
                if filtro == tarefa.status or filtro == tarefa.prioridade:
                    print(tarefa)
            else:
                print(tarefa)

    def excluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            print("Tarefa excluída com sucesso.")
        else:
            print("Índice inválido.")



gerenciador = GerenciadorDeTarefas()

gerenciador.criar_tarefa("Lista Dorival", "Alta", "2025-01-24", "Estudos")

print("\nTodas as tarefas:")
gerenciador.listar_tarefas()

print("\nTarefas com prioridade 'Alta':")
gerenciador.listar_tarefas(filtro="Alta")

print("\nTarefas concluídas:")
gerenciador.listar_tarefas(filtro="Concluída")

gerenciador.excluir_tarefa(1)

print("\nTodas as tarefas após exclusão:")
gerenciador.listar_tarefas()
