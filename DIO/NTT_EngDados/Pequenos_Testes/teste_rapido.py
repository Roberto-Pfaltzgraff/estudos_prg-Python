# A função len() é um exemplo de polimorfismo
# pois no 1º caso é passado como parâmetro uma string
# e o comportamento é contar a quantidade de caracteres desta string.
# no 2º caso é passado uma lista de valores inteiros
# e o comportamento é outro, agora contar a quantidade de elementos da lista
print(len("python"))
print(len([10, 20, 30]))

# Outro exemplo de polimorfismo é a função print()
# que muda e muito as variações de sua forma, ou seja,
# as muitas formas de passar paramentro para ela e com tipos diferentes.
# Ora string, número(inteiro, float, etc), datetime, lista, dicionário, objeto, etc)
# além de poder receber o usual de 1 parâmentro, nenhum ou muitos
print(10)
print()
print("nome")
print([10, 20, 30])
print("Maria", 20, "anos")

# Comentários com anotações especiais
# TODO: Veja que também não precisa de : TODO
# Mesma coisa vale para o FIXME também realça