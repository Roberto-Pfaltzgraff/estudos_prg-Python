print("TESTES: 01 - Valores diferentes!")
saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

print("TESTES: 02 - Valores iguais e mesmas variaveis!")
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

print("TESTES: 03 - com Strings!")
texto_1 = "ABC"
texto_2 = "ABZd"

print(texto_1 is texto_2)
print(texto_1 is not texto_2)

texto_2 = "ABC"

print(texto_1 is texto_2)
print(texto_1 is not texto_2)
