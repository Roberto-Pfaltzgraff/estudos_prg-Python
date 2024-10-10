# Declaração das Variaveis para Testa métodos de INTERPOLAÇÃO
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

nome = "Maria José"
idade = 32
profissao = "Programadora"
linguagem = "Python"

# Definindo Dicionário
pessoa = {"nome_pessoa": "Guilherme", "idade_pessoa": 28, "profissao_pessoa": "Programador", "linguagem_pessoa": "Python"}


# Método Old style %
print("***** Método: % (Old style) *****")
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou estudando %s." % (nome, idade, profissao, linguagem))
print("Nome: %s. Idade: %d. Profissão: %s. Curso: %s." % (nome, idade, profissao, linguagem))


# Método Format {}
print("***** Método: Format {} *****")
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou estudando {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {1}. Eu tenho {0} anos de idade, trabalho como {2} e estou estudando {3}.".format(idade, nome, profissao, linguagem))
# Meu teste do Format com reutilização da mesma variavel/valor
print("Olá, me chamo {1}. Eu tenho {0} anos de idade, trabalho como {2} e estou estudando {3}. Melhorando como {2}!".format(idade, nome, profissao, linguagem))
# Outra variação do Format
print("Olá, me chamo {name}. Eu tenho {age} anos de idade, trabalho como {professional} e estou estudando {curse}.".format(name=nome, age=idade, professional=profissao, curse=linguagem))
print("Olá, me chamo {name}. Eu tenho {age} anos de idade, trabalho como {professional} e estou estudando {curse}. Melhorando como {professional}!".format(name=nome, age=idade, professional=profissao, curse=linguagem))
# Usando Dicionário
print("Olá, me chamo {nome_pessoa}. Eu tenho {idade_pessoa} anos de idade, trabalho como {profissao_pessoa} e estou estudando {linguagem_pessoa}.".format(**pessoa))
print("Olá, me chamo {nome_pessoa}. Eu tenho {idade_pessoa} anos de idade, trabalho como {profissao_pessoa} e estou estudando {linguagem_pessoa}. Melhorando como {profissao_pessoa}!".format(**pessoa)) # Meu teste do Format com reutilização da mesma variavel/valor
# Resumo de todas do Format
print("Nome: {}. Idade: {}. Profissão: {}. Curso: {}.".format(nome, idade, profissao, linguagem))
print("Nome: {0}. Idade: {1}. Profissão: {2}. Curso: {3}. Repetindo idade: {1}.".format(nome, idade, profissao, linguagem))
print("Nome: {name}. Idade: {age}. Profissão: {prof}. Curso: {curse}. Repetindo idade: {age}.".format(name=nome, age=idade, prof=profissao, curse=linguagem))
print("Nome: {nome_pessoa}. Idade: {idade_pessoa}. Profissão: {profissao_pessoa}. Curso: {linguagem_pessoa}.. Repetindo idade: {idade_pessoa}.".format(**pessoa))

# Método f-string
print("***** Método: f-string (The best in my opnion) *****")
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou estudando {linguagem}.")
print(f"Nome: {nome}. Idade: {idade}. Profissão: {profissao}. Curso: {linguagem}.")


# Formatando strings com f-string
print("***** Formatando strings com f-string *****")
PI = 3.14159

print(f"Valor de PI: {PI}")
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:.4f}")
print(f"Valor de PI: {PI:0.2f}")
print(f"Valor de PI: {PI:10.2f}")
