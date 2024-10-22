# 1) Importação do Módulo e Classe ABC (Possibilita classes abstratas)
from abc import ABC, abstractmethod, abstractproperty

# Tornou-se uma classe abstrata por possuir método abstrato
class ControleRemoto:
    @abstractmethod    # 2) Torna o método abstrato (O método abstrato não pode ser instanciado. Serve de base para implementação nas subclasses)
    def ligar(self):
        pass

    @abstractmethod    # 2) Torna o método abstrato (O método abstrato não pode ser instanciado. Serve de base para implementação nas subclasses)
    def desligar(self):
        pass

    # É possível trabalhar com o conceito de propriedade em classes abstratas
    # Para isso é necessário utilizar o método já conhecido @property
    # seguido do método @abstractproperty
    @property
    @abstractproperty
    def marca(self):
        pass

# Sendo uma classe derivada de uma classe abstrata
# será obrigada a implementar os métodos especificados na classe abstrata como tais métodos abstratos
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV.......\nLigada!")
        # return super().ligar() # Veio no autocomplete da IDE, mas não foi necessária.

    def desligar(self):
        print("Desligando a TV.......\nDesligada!")
        # return super().ligar() # Veio no autocomplete da IDE, mas não foi necessária.

    # O método derivado do método abstrato também precisa DECORAR o @property
    @property
    def marca(self):
        return "Samsung"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a Ar Condicionado.......\nLigado!")

    def desligar(self):
        print("Desligando a Ar Condicionado.......\nDesligado!")

    # O método derivado do método abstrato também precisa DECORAR o @property
    @property
    def marca(self):
        return "Consul"

# ***** main *****
controle = ControleTV()
controle.ligar()
controle.desligar()

controle_ar = ControleArCondicionado()
controle_ar.desligar()
controle_ar.ligar()

print("\nMarca da TV:", controle.marca)
print("\nMarca da Ar Condicionado:", controle_ar.marca)
