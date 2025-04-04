class Retangulo:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width
    
    def area(self):
        area = self.width*self.width
        return area
    
    def perimeter(self):
        perimeter = 2*(self.width+self.heigth)
        return perimeter
    

heigth = float(input("Digite uma altura: "))
width = float(input("Digite uma largura: "))

retangulo = Retangulo(heigth, width)

print(f"Área: {retangulo.area}, Perímetro: {retangulo.perimeter}")