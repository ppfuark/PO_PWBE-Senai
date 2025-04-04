import random

class Personagem:
    def __init__(self, nome, saude, forca, defesa, habilidade_especial):
        self.nome = nome
        self.saude = saude
        self.forca = forca
        self.defesa = defesa
        self.habilidade_especial = habilidade_especial

    def atacar(self, alvo):
        dano = max(0, self.forca - alvo.defesa)
        alvo.saude -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        return dano

    def usar_habilidade_especial(self, alvo):
        if self.habilidade_especial == "Cura":
            quantidade_cura = 15
            self.saude += quantidade_cura
            print(f"{self.nome} usou sua habilidade especial e recuperou {quantidade_cura} de saúde!")
        elif self.habilidade_especial == "Golpe Duplo":
            print(f"{self.nome} usou Golpe Duplo!")
            self.atacar(alvo)
            self.atacar(alvo)

    def usar_item(self, item):
        if item == "Poção de Cura":
            quantidade_cura = 20
            self.saude += quantidade_cura
            print(f"{self.nome} usou uma {item} e recuperou {quantidade_cura} de saúde!")

    def esta_vivo(self):
        return self.saude > 0


def combate(jogador, inimigo):
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\n{jogador.nome} - Saúde: {jogador.saude}")
        print(f"{inimigo.nome} - Saúde: {inimigo.saude}")

        acao = input("Escolha sua ação (atacar, especial, item): ").lower()
        if acao == "atacar":
            jogador.atacar(inimigo)
        elif acao == "especial":
            jogador.usar_habilidade_especial(inimigo)
        elif acao == "item":
            jogador.usar_item("Poção de Cura")
        else:
            print("Ação inválida!")

        if not inimigo.esta_vivo():
            print(f"\n{inimigo.nome} foi derrotado! {jogador.nome} venceu!")
            break

        acao_inimigo = random.choice(["atacar", "especial"])
        if acao_inimigo == "atacar":
            inimigo.atacar(jogador)
        elif acao_inimigo == "especial":
            inimigo.usar_habilidade_especial(jogador)

        if not jogador.esta_vivo():
            print(f"\n{jogador.nome} foi derrotado! {inimigo.nome} venceu!")


jogador = Personagem(nome="Sim", saude=100, forca=20, defesa=10, habilidade_especial="Golpe 2x")
inimigo = Personagem(nome="Nao", saude=100, forca=20, defesa=10, habilidade_especial="Cura")

combate(jogador, inimigo)
