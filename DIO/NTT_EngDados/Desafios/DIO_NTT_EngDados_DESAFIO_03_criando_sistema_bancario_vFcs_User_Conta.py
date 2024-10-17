# Desafio do BootCamp DIO & NTT Data Engenharia de Dados com Python (Desafio 3 - Funções, Usuários e Contas)
# Objetivo: 
#     Alterar o sistema bancário criado anteriormente nos desafio para implementar novas funcionalidades.
#     Usar funções, criar operação de cadastro de usuário e de conta.
#        1) XXXX;
#        2) XXXX;
#        3) XXXX.
#     O intuito é aplicar tudo que foi aprendido até essa etapa.
# Ponto de Partida (Código que fiz no 2º Desafio):
#     https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/DIO_NTT_EngDados_DESAFIO_02_criando_sistema_bancario_vData_Minha.py
#     https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/aREADME_Desafio_02_criando_sistema_bancario_vData.md

# *** Módulos necessários ***
from datetime import datetime, date, time, timedelta # Por enquanto sem necessidade: , timezone

# *** Declaração de constates ***
C_MENU = """

*************** MENU ***************

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite o número correspondente a opção desejada: """
C_QTD_MAX_SAQUES_DIA = 3 # Limite de realização de saque por dia
C_VALOR_MAX_POR_SAQUE = 500.00 # Limite máximo por saque
C_LIMITE_TRANSACOES_DIARIA = 10 # Quantidade máxima de transações por dia
C_NUM_SEGUNDOS_TEMPORIZADOR = 2 # Tempo em segundos da mensagem com temporizador

# *** Declaração de variáveis ***
v_opcao_menu = "0"
v_saldo = 0 # Futuramente Recuperar o Saldo por função.
v_extrato = "" # Para exibição do extrato e atualização das operaçoes de depósito e saque
v_qtd_saque_hoje = 0  # Controlar qtd de saques no dia # Futuramente controlar melhor por função.


# *** Declaração de funções ***
def fc_operacao_depositar(p_saldo, p_extrato):
    # Função responsável pela Operação Depositar
    # Regras: - Deve ser possível depositar valores positivos para minha conta bancária.
    #         - A versão v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos
    #           preocupar em identificar qual é o número da agência e conta bancária.
    #         - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato.
    # Parametros: Serão recebidos e atualizados com a operação realizada.
    print("Deposito")
    while True:
        # Funcionalidade 1 e 2: Tratamento limite diário de transações e mensagem
        if fc_excedeu_limite_transacoes_hoje(p_extrato_atual=p_extrato):
            fc_mensagem_temporizada("\n\nO limite de transações diária foi atingindo.\nEssa operação está sendo cancelada.\n<<<Retornando ao Menu!>>>", C_NUM_SEGUNDOS_TEMPORIZADOR)
            break
        # Ler valor a depositar
        v_valor_deposito = fc_ler_valor_monetario("Digite um valor positivo para o DEPÓSITO ou 0 (zero) p/ cancelar a operação e retornar ao menu.\nDigite o valor do depósito: R$ ")
        if v_valor_deposito < 0:
            print("ATENÇÃO! Não é possível fazer depósito com valor NEGATIVO!")
            continue
        elif v_valor_deposito == 0:
            fc_mensagem_temporizada("\n\nOperação de depósito cancelada. Retornando ao Menu!", C_NUM_SEGUNDOS_TEMPORIZADOR)
            break
        else:
            p_saldo += v_valor_deposito
            # Funcionalidade 3: Inserção da Data e Hora no Extrato & Melhoria
            v_inicio_extrato = "" if not p_extrato else "\n"
            v_str_data_hora = fc_str_data_hora_atual(p_so_data=False)
            p_extrato += f"{v_inicio_extrato}Data hora: {v_str_data_hora} | Operação: Depósito (+) = R$ {v_valor_deposito:.2f}"
            fc_mensagem_temporizada(p_mensagem=f"O valor de R$ {v_valor_deposito:.2f} foi depositado com sucesso!\nSeu saldo é de R$ {p_saldo:.2f}!", p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)
        break
    return p_saldo, p_extrato

def fc_operacao_sacar(p_saldo, p_extrato, p_qtd_saques_do_dia):
    # Função responsável pela Operação de Saque
    # Regras: - O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
    #         - Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando
    #           que não será possível sacar o dinheiro por falta de saldo.
    #         - Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.
    # Parametros: Serão recebidos e atualizados com a operação realizada.
    print("Saque")
    if p_qtd_saques_do_dia >= 3:
        fc_mensagem_temporizada("\n\nVocê alcançou o limite diário de 3 saques!\nLogo, não poderá prosseguir com a operação de saque.", C_NUM_SEGUNDOS_TEMPORIZADOR)
        return p_saldo, p_extrato, p_qtd_saques_do_dia
    while True:
        # Funcionalidade 1 e 2: Tratamento limite diário de transações e mensagem
        if fc_excedeu_limite_transacoes_hoje(p_extrato_atual=p_extrato):
            fc_mensagem_temporizada("\n\nO limite de transações diária foi atingindo.\nEssa operação está sendo cancelada.\n<<<Retornando ao Menu!>>>", C_NUM_SEGUNDOS_TEMPORIZADOR)
            break
        # Ler valor a sacar
        v_valor_saque = fc_ler_valor_monetario("Digite um valor positivo para o SAQUE ou 0 (zero) p/ cancelar a operação e retornar ao menu.\nDigite o valor do saque: R$ ")
        if v_valor_saque < 0: # Futuramente: Passar esse tratamento e do deposito para fc_ler_valor_monetario
            print("ATENÇÃO! Não é possível fazer saque com valor NEGATIVO!")
            continue
        elif v_valor_saque == 0:
            fc_mensagem_temporizada("\n\nOperação de saque cancelada. Retornando ao Menu!", C_NUM_SEGUNDOS_TEMPORIZADOR)
            break
        elif v_valor_saque > C_VALOR_MAX_POR_SAQUE:
            fc_mensagem_temporizada(f"\n\nO valor máximo por saque é de R$ {C_VALOR_MAX_POR_SAQUE:.2f}.\nInforme um novo valor dentro do limite!", C_NUM_SEGUNDOS_TEMPORIZADOR)
            continue
        elif v_valor_saque > p_saldo:
            fc_mensagem_temporizada(f"\n\nO valor informado p/ saque de R$ {v_valor_saque:.2f} é maior que seu saldo de R$ {p_saldo:.2f}.\nNão é possível prosseguir com o saque por falta de saldo.\nInforme um novo valor de saque dentro do seu saldo!", C_NUM_SEGUNDOS_TEMPORIZADOR)
            continue
        else:
            p_qtd_saques_do_dia += 1
            p_saldo -= v_valor_saque
            # Funcionalidade 3: Inserção da Data e Hora no Extrato & Melhoria
            v_inicio_extrato = "" if not p_extrato else "\n"
            v_str_data_hora = fc_str_data_hora_atual(p_so_data=False)
            p_extrato += f"{v_inicio_extrato}Data hora: {v_str_data_hora} | Operação: Saque    (-) = R$ {v_valor_saque:.2f}"
            fc_mensagem_temporizada(p_mensagem=f"O valor de R$ {v_valor_saque:.2f} foi sacado com sucesso!\nSeu saldo atual é de R$ {p_saldo:.2f}!", p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)
        break
    return p_saldo, p_extrato, p_qtd_saques_do_dia

def fc_operacao_extrato(p_saldo, p_extrato):
    # Função responsável pela Operação de Extrato
    # Regras: - Essa operação deve listar todos os depósitos e saques realizados na conta.
    #         - Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
    #           Exemplo: 1500.45 ⇒ deve ser apresentado = R$ 1500.45.
    #         - No fim da listagem deve ser exibido o saldo atual da conta.
    # Parametros: Serão recebidos e exibidos com a operação realizada.
    C_QTD_CARACTERES_EXTRATO = 70
    print("Extrato\n\n")
    print("Extrato Bancário".center(C_QTD_CARACTERES_EXTRATO, "="))  # Cabeçalho
    print("Sua conta bancária não possui movimentações!" if not p_extrato else p_extrato) # Conteúdo da movimentação
    print("".center(C_QTD_CARACTERES_EXTRATO, "-"))  # Separador
    print(f"Seu Saldo atual é de R$ {p_saldo:.2f}.") # Exibindo Saldo
    fc_mensagem_temporizada("".center(C_QTD_CARACTERES_EXTRATO, "="), C_NUM_SEGUNDOS_TEMPORIZADOR)  # Rodapé


def fc_mensagem_temporizada(p_mensagem, p_tempo_em_segundos):
    # Função que apresenta a mensagem do parâmetro p_mensagem e realiza uma espera
    # aproximada de segundos definida no parâmetro p_tempo_em_segundos para prosseguir com o processamento.
    # Permitindo que o usuário leia a mensagem, antes de reapresentar novas mensagens.
    # Provavelmente há funções próprias para isso, mas será vista em módulos seguintes
    QTD_EQUIVALENTE_1SEGUNDO = 89000000 # Aproximadamente com testes feitos na maquina local
    qtd_repeticao_total = QTD_EQUIVALENTE_1SEGUNDO * p_tempo_em_segundos
    print(p_mensagem)
    # Laço para realizar uma espera com um temporizador de aproximadamente a quantidade de segundos desejada.
    for temporizador in range(qtd_repeticao_total):
        pass # Não faz nada.

def fc_ler_valor_monetario(p_mensagem):
    # Função irá apresentar uma mensagem antes leitura, conforme parâmetro
    # após digitação do usuário, irá validar a digitação para garantir
    # que a entrada seja um número monetário
    while True:
        str_valor = input(p_mensagem)
        if not str_valor.replace(".", "", 1).isdigit():
            print("ATENÇÃO! O valor digitado deve ser numérico.\n      Não pode conter letras e outros caracteres. Apenas digitos e um ponto decimal!")
            continue
        else:
            break
        break
    return float(f"{float(str_valor):.2f}")

def fc_str_data_hora_atual(p_so_data=False):
    # Funçao que retorna uma string com a atual Data e Hora ou apenas a Data formatada.
    # O formato seguirá respectivamente o padrão: "DD/MM/YYYY HH:MM" ou "DD/MM/YYYY".
    # Se o parâmetro p_so_data for:
    #         True => Retornará apenas a Data.
    #         False => Retornará a Data e Hora.
    return datetime.now().strftime("%d/%m/%Y") if p_so_data else datetime.now().strftime("%d/%m/%Y %H:%M")

def fc_qtd_transacoes_hoje(p_str_extrato):
    # Função que retorna a quantidade de transações no extrato realizada na data de hoje.
    # Parêmtro p_str_extrato irá receber a string com as movimentações do extrato.
    return p_str_extrato.count(fc_str_data_hora_atual(p_so_data=True))

def fc_excedeu_limite_transacoes_hoje(p_extrato_atual):
    # Função que irá verificar se a quantidade de transações excedeu o limite estabelecido.
    # Caso positivo, retorna True, senão False.
    return fc_qtd_transacoes_hoje(p_extrato_atual) >= C_LIMITE_TRANSACOES_DIARIA

# *** Programa Principal ***
while True:
    # Laço de interação do Menu
    v_opcao_menu = input(C_MENU)

    if v_opcao_menu == "0":
        print("Obrigado por ser nosso cliente e utilizar nossos serviços!")
        break

    elif v_opcao_menu == "1":
        v_saldo, v_extrato = fc_operacao_depositar(p_saldo=v_saldo, p_extrato=v_extrato)
    
    elif v_opcao_menu == "2":
        v_saldo, v_extrato, v_qtd_saque_hoje = fc_operacao_sacar(p_saldo=v_saldo, p_extrato=v_extrato, p_qtd_saques_do_dia=v_qtd_saque_hoje)
    
    elif v_opcao_menu == "3":
        fc_operacao_extrato(p_saldo=v_saldo, p_extrato=v_extrato)
    
    else:
        fc_mensagem_temporizada(p_mensagem="Opção inválida!\nFavor escolher uma das opções numéricas apresentada no menu.",
                                p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)
        continue
        print("Opção inválida!\nFavor escolher uma das opções numéricas apresentada no menu.")
