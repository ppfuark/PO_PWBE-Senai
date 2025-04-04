import random

class JogoCartas:
    def __init__(self, nome, qnt_cartas):
        self.nome = nome
        self.cores = ["azul", "verde", "roxo", "vermelho", "amarelo"]
        self.qnt_cartas = qnt_cartas
        self.cartas = []


    def embaralharCartas(self):
        if self.qnt_cartas < 30:
            self.qnt_cartas = 30
            print("A quantidade não pode ser menor que 30!")

        cartas = [None] * self.qnt_cartas

        for i in range(self.qnt_cartas):
            cartas[i] = random.choice(self.cores)
        
        for carta in cartas:
            self.cartas.append(carta)

    def distribuirCartas(self, qnt_cartas_destribuidas):
        if qnt_cartas_destribuidas > self.qnt_cartas:
            print("Quantidade inválida.")

    def jogar(self):
        if self.qnt_cartas <= 0:
            print("Sem cartas para jogar")
        else:
            carta_jogada = random.choice(self.cartas)
            self.cartas.remove(carta_jogada)
            print(f"{self.cartas}, {len(self.cartas)}")

jogador1 = JogoCartas("Ph",20)

jogador1.embaralharCartas()
jogador1.distribuirCartas(29)
jogador1.jogar()