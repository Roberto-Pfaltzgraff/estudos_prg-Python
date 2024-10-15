print("Passo 01: Inicialização & Alteração de valor da variável!")
saldo = 500
print(saldo)
saldo = 200
print(saldo)

print("Passo 02: Operadores de Atribuição!")

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo /= 2
print(saldo)

saldo //= 2
print(saldo)

saldo *= 10
print(saldo)

print("OBS na Divisão: Mesmo sendo uma operação entre 2 inteiros, e a variável inteira; o resultado da operação deste operador resulta sempre em float,")
print("logo o Python precisa converter o tipo dessa variável para poder receber o resultado sem perda de informação. Então, essa variável que era inteira passa a ser um float.")
print("")
print("OBS na Divisão Inteira: Caso a variável seja inteira, ela permanecerá sendo do tipo inteiro, pois o resultado do operador desta operação é um inteiro.")
print("Em contrapartida, se a variável for float, ela permanecerá sendo float, pois embora o resultado da divisão seja um inteiro, esse valor inteiro será atribuído a uma variável que já é float.")

print("")

print("Passo 03: Operadores de Atribuição (Módulo & Exponenciação)!")

saldo %= 4
print(saldo)

saldo **= 3
print(saldo)

print("FIM dos testes com Operadores de Atribuição!")