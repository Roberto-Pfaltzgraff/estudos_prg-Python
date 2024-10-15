nome = input("Informe o seu nome: ")
idade = input("Informe o seu idade: ")

print(nome, idade)
print("teste SEM")
print("teste COM", end=" ")
print(nome, idade, end='...\n')
print(nome, idade, end='...\n', sep="#")
print(nome, idade, sep="  |   ")