# O continue salta a execução para o início do laço/loop e próximo step/Passo dentro de um bloco de código de uma estrutura de repetição
# Vamos fazer o algoritmo para o jogo do Plim do Silvio Santos

for numero in range(1, 30+1):

    if numero % 3 == 0:
        print("PLIM", end=" ")
        continue

    print(numero, end=" ")
