class Aluno:
    def __init__(self, name, registration):
        self.name = name
        self.registration = registration
        self.grade = []
    
    def add_grades(self, value):
        self.grade.append(value)

    def gradeAverage(self):
        count = sum(self.grade)
        average = count/len(self.grade)
        return average
    
    def situation(self):
        if aluno.gradeAverage() >= 5:
            return "Aprovado!"
        else:
            return "Reprovado"

aluno = Aluno('Paulo', 123)    

qntNotas = int(input("Digite a quantidade de notas: "))

for i in range(qntNotas):
    nota = float(input(f"Digite a nota {i+1}: "))
    aluno.add_grades(nota)

print(f"Média: {aluno.gradeAverage()}, Situação: {aluno.situation()}")