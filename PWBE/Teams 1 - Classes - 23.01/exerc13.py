class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato '{nome}' já está na agenda.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")

    def editar_contato(self, nome, novo_telefone):
        if nome in self.contatos:
            self.contatos[nome] = novo_telefone
            print(f"Telefone do contato '{nome}' atualizado para {novo_telefone}.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def buscar_por_nome(self, nome):
        if nome in self.contatos:
            telefone = self.contatos[nome]
            print(f"Contato encontrado: {nome} - {telefone}")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def buscar_por_telefone(self, telefone):
        for nome, numero in self.contatos.items():
            if numero == telefone:
                print(f"Contato encontrado: {nome} - {telefone}")
                return
        print(f"Número '{telefone}' não encontrado na agenda.")

agenda = Agenda()

agenda.adicionar_contato("João", "1234-5678")
agenda.adicionar_contato("Maria", "9876-5432")

agenda.editar_contato("João", "4321-8765")

agenda.remover_contato("Maria")

agenda.buscar_por_nome("João")
agenda.buscar_por_telefone("4321-8765")
