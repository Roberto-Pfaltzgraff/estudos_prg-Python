class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Sem o método de classe. Vide comentário em main na atribuição de p2
    def criar_apartir_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 -ano
        return Pessoa(nome, idade)
    
    # Com o método de classe. Vide comentário em main na atribuição de p3
    @classmethod
    def criar_apartir_ano_nascimento(cls, ano, nome):
        print(cls) # Mostra que é a classe Pessoa e não a instancia: <class '__main__.Pessoa'>
        idade = 2024 -ano
        # return Pessoa(nome, idade)
        return cls(nome, idade) # Utilizando cls(), refenciamos o proprio objeto e não um novo como seria com Pessoa()
    
    # Método estático
    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18

# ***** main *****

# Forma normal
p1 = Pessoa("Guilherme", 28)
print(p1.nome, p1.idade)

# Criando por outro metodo sem ser o construtor
# Problema: Desta forma estão sendo criado 2 objetos apenas com o comando abaixo.
# O Pessoa() neste comando por si só cria um objeto. E a partir desse objeto
# com a chamada do método tradicional é criado um novo objeto quando dá o return Pessoa(nome, idade)
# para p2 é retornado apenas 1 objeto e é o que interessa: com o nome e idade.
# Mas o código não está eficiente, pois criar um objeto desnecessário.
p2 = Pessoa().criar_apartir_data_nascimento(1994, 6, 15, "Denise")
print(p2.nome, p2.idade)

# Criando o objeto com o método de classe.
# OBS: Que referenciamos a classe direto com Pessoa. e não como no exemplo anterior que era Pessoa().
p3 = Pessoa.criar_apartir_ano_nascimento(1992, "Giulianna")
print(p3.nome, p3.idade)

# Executanto o método estático
# Para acioná-lo deve primeiro referenciar a classe, seguido do . e o nome do método
r1 = Pessoa.eh_maior_idade(18)
r2 = Pessoa.eh_maior_idade(8)
r3 = Pessoa.eh_maior_idade(48)
print(r1, r2, r3)
print(p1.eh_maior_idade(p1.idade)) # Ocorre erro, se...
# ... Se o @staticmethod que define o método estático for retirado de sua definição
# essa ultima linha irá gerar erro ao executar o código.
# isso porque o método está sendo acionado pela instancia
# e nesse caso é um método normal que requer o 1º argumento, self, que é a referencia da instancia
# e na definição do eh_maior_idade() não tá definido o self, apenas idade.
# Por isso, a necessidade do @staticmethod, uma vez que neste caso nós não queremos essa obrigação da instancia.