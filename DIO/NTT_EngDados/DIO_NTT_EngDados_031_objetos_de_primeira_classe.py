# Definição da função somar() que terá seu nome passado como parâmetro em outra função
def somar(a, b):
    return a + b

# Definição da função exibir_resultado() que irá receber o nome de outra função como parâmetro
# depois, entre seus comandos, irá executar a função que foi recebido o nome no parâmetro
def exibir_resultado(p1, p2, pfuncao):
    resultado = pfuncao(p1, p2) # Nesta parte do código, ocorre a chamada da função, antes foi só referência
    print(f"O resultado da operação {p1} + {p2} = {resultado}")


# Programa principal
# chamando a função exibir_resultado, passando apenas o nome da função somar, sem executá-la na chamada, pois não é somar() com os parenteses
exibir_resultado(20, 30, somar)

# Também pode ser feito com variável, assim:
executa = somar
print(f"Executa soma. Resultado é = {executa(40, 30)}.")