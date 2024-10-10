MAIOR_IDADE = 18
TERCEIRA_IDADE = 65
IDADE_EMACIPADO = 14

idade = int(input("Informe sua idade: "))

if idade >= TERCEIRA_IDADE:
    print("Encontra-se na 3ª idade, será necessário exames especiais para tirar/renovar a CNH. (+65anos)")

elif idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH. (Adulto)")

elif idade >= IDADE_EMACIPADO:
    print("Menor de idade, pode tirar a CNH apenas se for EMACIPADO financeiramente ou profissionalmente. (a partir dos 14anos)")

else:
    print("Não se enquadra em nenhuma faixa etária permitida, NÃO pode tirar a CNH.")

print("\n\n*** OBSERVE que ao encontrar a 1ª condição que atenda a expressão como verdadeira, os demais <elif>s não são executados. ***")
