# Definindo uma classe chamada Bicicleta
class Bicicleta:
    # Método construtor - Chamado automaticamente ao instanciar o objeto desta classe de objetos
    def __init__(self, cor, modelo, ano, valor):
        # Definindo os atributos desta classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    # Métodos da classe - Estes Métodos/Funções são os comportamentos
    # dos objetos que forem instanciados por esta classe
    def buzinar(self):
        print("Bi bi...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmm")
    
    # Método __str__ define um retorno para o objeto quando este
    # for utilizado diretamente sem apontar para um atributo ou método
    # aqui teremos mais de uma forma, faça os testes com todos
    # comentados, depois vá alterando as ativações
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#    def __str__(self):
#        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano} e valor={self.valor}."


# Instanciando uma Bicicleta e dando o nome desse objeto de b1
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Executando os métodos do objeto
b1.buzinar()
b1.correr()
b1.parar()

# Acessando e exibindo os atributos do objeto
print(b1.cor, b1.modelo, b1.ano, b1.valor)


# O Python preenche o self automaticamente com
# o nome do objeto que estamos tentando instaciar.
# Vamos instanciar um 2º objeto e vê a outra forma
# de fazer isso que o Python já faz de forma automatica
b2 = Bicicleta("verde", "monark", 2000, 189)
# Para o construtor isso não funciona. Até porque não é o nome do método
# a chamada abaixo gera erro se descomenta-la e comentar a anterior
#Bicicleta(b2, "verde", "monark", 2000, 189)
print("\n" * 3)
print(b2.cor, b2.modelo, b2.ano, b2.valor)
# Já essa forma de chamar o método funciona
Bicicleta.buzinar(b2)
# E é equivalente a essa forma tradicional
b2.buzinar()

# Testes do método __str__
# Veja o comentário na classe
# sem o __str__, retornará algo desse tipo:
# <__main__.Bicicleta object at 0x0000024B0A57A8D0>
print(b2)