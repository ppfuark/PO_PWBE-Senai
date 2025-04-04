pi = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius

radius = float(input("Digite um raio: "))

circle = Circle(radius)

print(f"Área: {circle.calculate_area():.2f}, Perímetro: {circle.calculate_perimeter():.2f}")
