class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0

    def velocidade(self):
        return self.velocidade

carro = Carro("Toyota", "Corolla")
carro.acelerar(20)
carro.frear(5)
print(f"Velocidade atual do carro: {carro.velocidade()} km/h")
