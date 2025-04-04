class Funcionario:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def net_salary(self, tax, benefit):
        self.salary += benefit
        taxedSalary = self.salary*tax
        liquid_salary = self.salary - taxedSalary
        return f"Salario líquido: R${liquid_salary}"

funcionario = Funcionario("Paulo Henrique", 1412, "Aprendiz")
print(funcionario.net_salary(float(input("Digite a taxa em decimal (48% -> 0.48): ")), float(input("Digite os benefícios: "))))