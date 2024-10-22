class Passaro:
    def voar(self):
        print("Voando (O Passáro)....")

class Canario(Passaro):
    def voar(self):
        super().voar()

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa...")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz NÃO voa...")

def plano_de_voo(objeto_qualquer):
    objeto_qualquer.voar()

pardal = Pardal()
avestruz = Avestruz()
canario = Canario()

plano_de_voo(pardal)
plano_de_voo(avestruz)
plano_de_voo(canario)

# Pode ser assim também:
plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Canario())