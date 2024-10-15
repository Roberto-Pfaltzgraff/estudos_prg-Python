# Exemplos de Criação de Listas em Python

# 1) Colocando valores separados por vírgula dentro de colchetes
frutas = ["laranja", "maca", "uva"]
legumes = []  # Lista vazia
carro = ["Ferrari", "F8", 420000, 2020, "ABC-1234", "RJ", True] # Lista com tipos diferentes
print(frutas)
print("".center(50,"-"))
print(legumes)
print("".center(50,"-"))
print(carro)
print("".center(50,"-"))

# 2) Com o construtor list
letras = list("python")
print(letras)
print("".center(50,"-"))

# 3) Com a função range()
numeros = list(range(10))
faixa = range(10) # Não gera uma lista. Eu quis fazer esse teste, pois achava que gerasse uma lista, devido a forma como usamos no for.
print(numeros)
print("".center(50,"-"))
print(faixa)
