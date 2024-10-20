class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor!")

    def __str__(self):
        return f"{self.__class__.__name__}:::"
    
    def __del__(self):
        print(f"TERMINOU ===> {self.__class__.__name__}.")


class Motocicleta(Veiculo):
    def tem_diferenca(self):
        print("Sim. Tenho descanso!")

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim," if self.carregado else "Não"} estou carregado!")

print("\n" + "INICIO".center(50, "*"))

print("\n" + "Veículo".center(50, "*"))
veiculo = Veiculo("ocre", "FFF-7777", 2)
veiculo.ligar_motor()
print(veiculo)

print("\n" + "Moto".center(50, "*"))
moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()
moto.tem_diferenca()
print(moto)

print("\n" + "Carro".center(50, "*"))
carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()
# carro.esta_carregado() # Ocorre erro pq esse método só existe na classe caminhão
print(carro)

print("\n" + "Caminhão".center(50, "*"))
caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)

print("\n" + "FIM".center(50, "*"))