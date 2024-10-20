class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}::: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    # O ornitorrinco é apenas mamífero. Existe uma particularidade de colocar ovos
    # e as patas que se assemelham a do pato, mas não é uma ave cientificamente falando.
    # Mas para fins deste exercicio e pela particularidade semelhante ao pato,
    # vamos considerar que ele seja um mamifero e ave.
    pass


# Herança Múltipla, ao instanciar a classe, é necessário realizar a passagem de parâmetro por Nomeação
cao = Cachorro(nro_patas=4, cor_pelo="preto")
print(cao)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)