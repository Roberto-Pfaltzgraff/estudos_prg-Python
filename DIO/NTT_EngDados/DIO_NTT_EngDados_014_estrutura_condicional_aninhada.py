conta_normal = not True
conta_universitaria = not False
conta_especial = not False

saldo = 2000
saque = 5000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
elif conta_especial:
    print("Conta especial selecionada!")
else:
    print("Sistema não reconheceu o tipo de conta. Entre em contato com seu gerente!")
