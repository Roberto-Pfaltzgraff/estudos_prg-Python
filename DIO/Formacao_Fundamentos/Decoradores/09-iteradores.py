class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    
    # Em uma classe, os métodos __iter__() e __next__()
    # são os que a classificam como iterável
    def __iter__(self):      # Importante para que a classe seja iteradora
        print("Debug >>> __Iter__()")
        return self
    
    def __next__(self):      # Importante para que a classe seja iteradora
        print("Debug >>> __Next__() - Entrou")
        try:
            valor = self.numeros[self.contador]
            self.contador += 1
            print("Debug >>> __Next__() - RETURNNNNNNNNN")
            return valor
        except IndexError:
            print("Debug >>> __Next__() - raiseeeeeeeeee")
            raise StopIteration

# *** Programa Principal ***
for numero in MeuIterador([1, 2, 3]):
    print(f"Main() ===> {numero}")
