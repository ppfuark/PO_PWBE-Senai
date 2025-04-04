class Animal:
    def __init__(self, nome, especie, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta
        self.habitat = habitat

    def alimentar(self):
        print(f"{self.nome} ({self.especie}) foi alimentado com {self.dieta}.")

    def verificar_saude(self):
        print(f"A saúde de {self.nome} foi verificada pelo veterinário.")

    def mover(self):
        print(f"{self.nome} se moveu.")

class Habitat:
    def __init__(self, nome):
        self.nome = nome

class Veterinario:
    def __init__(self, nome):
        self.nome = nome

    def realizar_exame(self, animal):
        print(f"{self.nome} realizou um exame em {animal.nome}.")

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def realizar_tarefa(self):
        print(f"{self.nome} ({self.cargo}) realizou sua tarefa no zoológico.")


habitat1 = Habitat("Savana")
animal1 = Animal("Simba", "Leão", "Carne", habitat1.nome)

veterinario = Veterinario("João")
funcionario = Funcionario("Ana", "Cuidadora")

animal1.alimentar()
animal1.mover()
veterinario.realizar_exame(animal1)
funcionario.realizar_tarefa()
