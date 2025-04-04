import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_gerado = random.randint(1, 100)

    def fazer_palpite(self, palpite):
        if palpite == self.numero_gerado:
            print("Parabéns! Você acertou!")
            return True
        elif palpite < self.numero_gerado:
            print("Errado! O número é maior.")
        else:
            print("Errado! O número é menor.")
        return False
