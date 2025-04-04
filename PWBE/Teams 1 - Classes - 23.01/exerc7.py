import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def valido(self):
        return (self.lado1 + self.lado2 > self.lado3) and (self.lado2 + self.lado3 > self.lado1) and (self.lado3 + self.lado1 > self.lado2)

    def area(self):
        if not self.valido():
            return "Não é um triângulo válido."
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

triangulo = Triangulo(3, 4, 5)
print("Triângulo válido?", triangulo.valido())
print(f"Área do triângulo: {triangulo.area()}")
