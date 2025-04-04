class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.consultas = []

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def consultas(self):
        return self.consultas

paciente = Paciente("Maria", 30)
paciente.adicionar_consulta("Consulta de rotina - 10/01/2025")
paciente.adicionar_consulta("Consulta de emergência - 15/01/2025")
print("Histórico de consultas:", paciente.consultas())
