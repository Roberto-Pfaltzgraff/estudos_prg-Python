# O break normalmente utilizado no while para interromper o fluxo de repetição
while True:
    numero = int(input("Informe um número (10 para sair!): "))
    
    if numero == 10:
        break
    
    print(numero)


# O break também funciona com o for
for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")
