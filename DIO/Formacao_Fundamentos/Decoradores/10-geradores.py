def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero ** 2

# Programa Principal
for valor_ao_quadrado in meu_gerador([1, 2, 3, 4, 5]):
    print(valor_ao_quadrado)