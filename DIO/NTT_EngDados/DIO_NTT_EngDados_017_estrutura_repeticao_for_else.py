texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()   # adiciona uma quebra de linha
    print("Executa somente no final do laço/loop!")

print("Já esta execução, ocorre fora do laço/loop!")
