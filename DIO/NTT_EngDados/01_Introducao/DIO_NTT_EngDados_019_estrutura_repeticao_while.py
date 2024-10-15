opcao = -1

while opcao != 0:
    opcao = int(input("Escolha a opção desejada:\n   [1] Sacar\n   [2] Extrato\n   [3] Mais opções\n   [0] Sair\nDigite o número correspondente a opção desejada: "))

    if opcao == 1:
        print("Sacando...prepare a manchete!")
    elif opcao == 2:
        print("Exibindo o extrato...de tomate! Rsrs.")
    elif opcao == 3:
        print("Abrindo o menu de mais opções...aceita um café de entrada?")
    elif opcao == 0:
        print("Obrigado por ser nosso cliente! Até logo!")
    else:
        print("Opção invalida!")

