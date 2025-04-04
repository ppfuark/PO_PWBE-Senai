class Peca:
    def __init__(self, cor):
        self.cor = cor

    def mover(self):
        print(f"{self.__class__.__name__} se moveu")

    def atacar(self):
        print(f"{self.__class__.__name__} atacou")

class Peao(Peca):
    def mover(self):
        print("Peão moveu uma casa para frente")

    def atacar(self):
        print("Peão atacou na diagonal")

    def promocao(self):
        print("Peão foi promovido")

    def en_passant(self):
        print("Peão capturou en passant")

class Torre(Peca):
    def mover(self):
        print("Torre moveu em linha reta")

class Cavalo(Peca):
    def mover(self):
        print("Cavalo moveu em L")

class Bispo(Peca):
    def mover(self):
        print("Bispo moveu na diagonal")

class Rainha(Peca):
    pass

class Rei(Peca):
    def roque_curto(self):
        print("Rei realizou o roque curto")
    def roque_longo(self):
        print("Rei realizou o roque longo")


p1 = Peao("branco")
t1 = Torre("preto")
r1 = Rei("branco")
ra1 = Rainha("branca")

p1.mover()
p1.atacar()
p1.en_passant()


ra1.mover()
t1.mover()
r1.mover()
r1.roque_curto()
