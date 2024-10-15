print("Tabela verdade do Operadores E (and) e OU (or)!")

print("E (and)")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("OU (or)")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("")
print("Exemplo do controle bancário de Saldo, Saque e Limite!")
saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao_parenteses = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_parenteses)

print("")
print("Ainda neste Exemplo, podemos quebrar a expressão em expressões menores e mais semânticas!")
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

expressao_conta_com_saldo_suficiente = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_conta_com_saldo_suficiente)


print("")
print("Meus Testes de Precedencias!")

print("Primeiro Teste: and or and!")
expressao_logica_01 = True and True or True and True
expressao_logica_02 = True and True or True and False
expressao_logica_03 = True and True or False and True
expressao_logica_04 = True and True or False and False

expressao_logica_05 = True and False or True and True
expressao_logica_06 = True and False or True and False
expressao_logica_07 = True and False or False and True
expressao_logica_08 = True and False or False and False

expressao_logica_09 = False and True or True and True
expressao_logica_10 = False and True or True and False
expressao_logica_11 = False and True or False and True
expressao_logica_12 = False and True or False and False

expressao_logica_13 = False and False or True and True
expressao_logica_14 = False and False or True and False
expressao_logica_15 = False and False or False and True
expressao_logica_16 = False and False or False and False

print(expressao_logica_01)
print(expressao_logica_02)
print(expressao_logica_03)
print(expressao_logica_04)
print(expressao_logica_05)
print(expressao_logica_06)
print(expressao_logica_07)
print(expressao_logica_08)
print(expressao_logica_09)
print(expressao_logica_10)
print(expressao_logica_11)
print(expressao_logica_12)
print(expressao_logica_13)
print(expressao_logica_14)
print(expressao_logica_15)
print(expressao_logica_16)

print("")
print("Último Teste: or and or!")
expressao_logica_01 = True or True and True or True
expressao_logica_02 = True or True and True or False
expressao_logica_03 = True or True and False or True
expressao_logica_04 = True or True and False or False

expressao_logica_05 = True or False and True or True
expressao_logica_06 = True or False and True or False
expressao_logica_07 = True or False and False or True
expressao_logica_08 = True or False and False or False

expressao_logica_09 = False or True and True or True
expressao_logica_10 = False or True and True or False
expressao_logica_11 = False or True and False or True
expressao_logica_12 = False or True and False or False

expressao_logica_13 = False or False and True or True
expressao_logica_14 = False or False and True or False
expressao_logica_15 = False or False and False or True
expressao_logica_16 = False or False and False or False

print(expressao_logica_01)
print(expressao_logica_02)
print(expressao_logica_03)
print(expressao_logica_04)
print(expressao_logica_05)
print(expressao_logica_06)
print(expressao_logica_07)
print(expressao_logica_08)
print(expressao_logica_09)
print(expressao_logica_10)
print(expressao_logica_11)
print(expressao_logica_12)
print(expressao_logica_13)
print(expressao_logica_14)
print(expressao_logica_15)
print(expressao_logica_16)

print("")
print("Conclusão: Há precedencia entre os operadores lógicos.")
print("1º executa o (not)")
print("2º executa o (and)")
print("3º executa o (or)")
print("FIM")