class Estudante:
    # Variável de classe. Pois está definida logo após a definição do nome da classe.
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


# declarações da main
def mostrar_informacoes(*objs):
    for obj in objs:
        print(obj)

# main
gui = Estudante("Guilherme", 56451)
gio = Estudante("Giovanna", 17323)
mostrar_informacoes(gui, gio)

Estudante.escola = "Novo Valor"   # Atributo de Classe
gui.numero = 33333                # Atributo de Instância
mostrar_informacoes(gui, gio)

gui.escola = "Python"   # Atributo de Instância
gui.numero = 44444      # Atributo de Instância
mostrar_informacoes(gui, gio)

# Definição:
# Atributo de instância é único para cada objeto / instância.
# Isso significa que se alterarmos o valor do atributo de um objeto, não deverá afetar o mesmo atributo de outro objeto.
# Resultado:
# Guilherme (56451) - DIO
# Giovanna (17323) - DIO
# Guilherme (33333) - Novo Valor
# Giovanna (17323) - Novo Valor
# Guilherme (44444) - Python
# Giovanna (17323) - Novo Valor
# Conclusão (neste exemplo):
# Atributo(s) de classe ==> escola
# Atributo(s) de instância ==> nome e numero

# Mais 1 teste. Agora criando nova instancia / objeto com as modificações realizadas
chp = Estudante("Chappie", 55231)
mostrar_informacoes(gui, gio, chp)

# Em RESUMO:
# Quando está logo após a definição da classe é Variável de Classe
# Quando tem o self na sua definição na classe é Variável de Instancia

Estudante.escola = "Novo Valor"   # Atributo de Classe
mostrar_informacoes(gui, gio, chp)