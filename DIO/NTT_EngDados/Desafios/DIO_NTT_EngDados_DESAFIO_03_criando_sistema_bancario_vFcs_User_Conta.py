# Desafio do BootCamp DIO & NTT Data Engenharia de Dados com Python (Desafio 3 - Funções, Usuários e Contas)
# Objetivo: 
#     Alterar o sistema bancário criado anteriormente nos desafio para implementar novas funcionalidades.
#     Usar funções, criar operação de cadastro de usuário e de conta.
#      1) Transformar as codificações das operações em funções ✅🆗(Já implementado desta forma na etapa 1)
#         - Cada operação precisa ser codificada como função.✅(Já tinha feito desta forma)
#         - A os argumentos das funções deve seguir a seguinte ordem:
#             - Função da operação **Saque** deve conter os argumentos apenas por nome (keyword only).
#             - Função da operação **Depósito** deve conter os argumentos apenas por posição (positional only).
#             - Função da operação **Extrato** deve conter os argumentos por posição e nome (positional only e keyword only). Sendo o argumento _saldo_ por posição e o argumento _extrato_ por nome.
#      2) Criar a função de Cadastrar Usuário (Cliente do banco)
#         - O sistema deve armazenar os usuários em uma lista.
#         - Um usuário é composto por: nome, data nascimento, cpf e endereço.
#         - O endereço é uma string com o formato: logradouro, número - bairro - cidade - sigla do estado.
#         - CPF deve conter apenas números.
#         - Não pode haver mais de 1 usuário com o mesmo CPF.
#      3) Criar a função de Cadastrar Conta Bancária (vincular com o Usuário/Cliente)
#         - O sistema deve armazenar as contas em uma lista.
#         - Uma conta é composta por: agência, número da conta e usuário.
#         - O número da conta é um sequencial, iniciado em 1.
#         - O número da agência é fixo: "0001"
#         - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário. 
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
[4] Cadastrar Usuário/Cliente
[5] Criar Conta Corrente
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
v_clientes = [] # Lista de Clientes / Usuários cadastrados (OBS: Lista cujo elementos são estruturas de dicionários)
v_contas = [] # Lista de Contas Bancárias cadastradas (OBS: Lista cujo elementos são estruturas de dicionários)

# *** Declaração de funções ***
def fc_operacao_depositar(p_saldo, p_extrato, /):
    # Função responsável pela Operação Depositar
    # Regras: - Deve ser possível depositar valores positivos para minha conta bancária.
    #         - A versão v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos
    #           preocupar em identificar qual é o número da agência e conta bancária.
    #         - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato.
    # Parametros: Serão recebidos argumentos apenas por posição e atualização de valores no retorno.
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

def fc_operacao_sacar(*, p_saldo, p_extrato, p_qtd_saques_do_dia):
    # Função responsável pela Operação de Saque
    # Regras: - O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
    #         - Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando
    #           que não será possível sacar o dinheiro por falta de saldo.
    #         - Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.
    # Parametros: Serão recebidos apenas por nome e atualização de valores no retorno.
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

def fc_operacao_extrato(p_saldo, /, *, p_extrato):
    # Função responsável pela Operação de Extrato
    # Regras: - Essa operação deve listar todos os depósitos e saques realizados na conta.
    #         - Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
    #           Exemplo: 1500.45 ⇒ deve ser apresentado = R$ 1500.45.
    #         - No fim da listagem deve ser exibido o saldo atual da conta.
    # Parametros: Serão recebidos o argumento saldo por posição e o argumento extrato por nome
    #             e a atualização de valores no retorno.
    C_QTD_CARACTERES_EXTRATO = 70
    print("Extrato\n\n")
    print("Extrato Bancário".center(C_QTD_CARACTERES_EXTRATO, "="))  # Cabeçalho
    print("Sua conta bancária não possui movimentações!" if not p_extrato else p_extrato) # Conteúdo da movimentação
    print("".center(C_QTD_CARACTERES_EXTRATO, "-"))  # Separador
    print(f"Seu Saldo atual é de R$ {p_saldo:.2f}.") # Exibindo Saldo
    fc_mensagem_temporizada("".center(C_QTD_CARACTERES_EXTRATO, "="), C_NUM_SEGUNDOS_TEMPORIZADOR)  # Rodapé

def fc_operacao_cadastra_cliente(p_lst_clientes):
    # Função responsável pelo Cadastro de Usuário/Cliente.
    # Regras/Funcionalidade:
    #    - Ler os dados de Cliente: CPF, Nome, Data Nascimento e Endereço
    #    - CPF será apenas números e não pode haver mais de um cadastrado na lista de Clientes
    #  Parâmetros: 
    #     - p_lst_clientes => Recebe a lista de Clientes cadastrados.
    #  Retorno: Será retornado a estrutura de dados do Cliente {CPF, Nome, Data Nascimento e Endereço}
    #           onde a funcionalidade chamadora irá integrá-la a respectiva lista de Clientes
    print("Cadastro Usuário/Cliente\n\n")
    while True:
        # Leitura e tratamento do CPF
        v_str_cpf = input("Digite o CPF do novo cliente (apenas digito): ")
        if not v_str_cpf.isdigit():
            print(f"ATENÇÃO! O valor digitado para CPF deve conter apenas digitos: {list(range(10))}!")
            continue
        else:
            # Futuramente implementar possibilidade de sair sem cadastrar e retornar ao menu
            v_cpf = int(v_str_cpf)
            
        # Verificar se esse CPF consta na lista de Clientes
        if [cliente.get("cpf") for cliente in p_lst_clientes if cliente.get("cpf") == v_cpf]:
            print("CPF informado já foi cadastrado! Não pode haver mais de um usuário com mesmo CPF. Informe um novo!")
            continue
        break
    v_nome = input("Digite o Nome: ")
    v_data_nascimento = input("Digite o Data de Nascimento (DD/MM/YYYY): ") # Futuramente implementar critica de validação e formatação
    v_endereco = input("Digite o Endereço (Logradouro, número - Bairro - Cidade - UF): ") # String sem tratamento, apenas indicando formato
    # Montar estrutura de dados de retorno para ser inserida na lista de Clientes
    v_novo_cliente = {"cpf": v_cpf, "nome": v_nome, "data_nascimento": v_data_nascimento, "endereco": v_endereco}
    return v_novo_cliente

def fc_operacao_criar_conta(p_lst_clientes, p_gerador_sequence):
    # Função responsável por Criar Conta Corrente Bancária.
    # Regras/Funcionalidade:
    #    - A Conta bancária é composta de: Agência, Conta e CPF (representando o Cliente/Usuário)
    #    - O número da Agência é fixo: "0001"
    #    - O número da Conta bancária é um seqêncial
    #    - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    #  Parâmetros: 
    #     - p_lst_clientes => Recebe a lista de Clientes cadastrados.
    #  Retorno: Será retornado a estrutura de dados da Conta {Agencia, Conta, CPF}
    #           onde a funcionalidade chamadora irá integrá-la a respectiva lista de Contas
    C_NUMERO_AGENCIA = "0001"
    print("Criar Conta Bancária\n\n")
    # Obter e validar CPF
    # Esse próximo trecho irá virar função p/ modularizar, mas não agora pois estou com foco no aprendizando das estruturas
    while True:
        # Leitura e tratamento do CPF
        v_str_cpf = input("Digite o CPF do Cliente para Nova Conta bancária (apenas digito): ")
        if not v_str_cpf.isdigit():
            print(f"ATENÇÃO! O valor digitado para CPF deve conter apenas digitos: {list(range(10))}!")
            continue
        else:
            # Futuramente implementar possibilidade de sair sem cadastrar e retornar ao menu
            v_cpf = int(v_str_cpf)
            
        # Confirmar se esse CPF consta na lista de Clientes
        if not [cliente.get("cpf") for cliente in p_lst_clientes if cliente.get("cpf") == v_cpf]:
            print("CPF informado não foi cadastrado! Para criar a Conta Bancária é necessário que o Cliente esteja cadastrado com seu CPF. Informe um existente!")
            continue
        break
    # Obtendo o número da conta bancária a ser criada
    v_numero_conta = next(p_gerador_sequence)
    # Montar estrutura de dados de retorno para ser inserida na lista de Contas
    v_nova_conta = {"agencia": C_NUMERO_AGENCIA, "conta": v_numero_conta, "cpf": v_cpf}
    return v_nova_conta

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

def fc_sequence_conta():
    # Função similar a uma sequence de banco para gerar o número sequencial
    # da conta bancária, começando em 1.
    v_sequencia = 0
    while True:
        v_sequencia += 1
        yield v_sequencia

# *** Programa Principal ***
v_gerador_sequence = fc_sequence_conta()
while True:
    # Laço de interação do Menu
    v_opcao_menu = input(C_MENU)

    if v_opcao_menu == "0":
        print("Obrigado por ser nosso cliente e utilizar nossos serviços!")
        break

    elif v_opcao_menu == "1":
        # Argumentos da Operação Depósito: p_saldo e p_extrato por posição apenas (Desafio 3)
        v_saldo, v_extrato = fc_operacao_depositar(v_saldo, v_extrato)
    
    elif v_opcao_menu == "2":
        # Argumentos da Operação Saque: p_saldo, p_extrato e p_qtd_saques_do_dia por nome apenas (Desafio 3)
        v_saldo, v_extrato, v_qtd_saque_hoje = fc_operacao_sacar(p_saldo=v_saldo, p_extrato=v_extrato, p_qtd_saques_do_dia=v_qtd_saque_hoje)
    
    elif v_opcao_menu == "3":
        # Argumentos da Operação Extrato: p_saldo por posição apenas e p_extrato por nome apenas (Desafio 3)
        fc_operacao_extrato(v_saldo, p_extrato=v_extrato)
    
    elif v_opcao_menu == "4":
        v_clientes.append(fc_operacao_cadastra_cliente(p_lst_clientes=v_clientes))
        # Visualizar Clientes/Usuários cadastrados. Solução temporária apenas para testes. Futuramente implementar funcionalidade no menu.
        fc_mensagem_temporizada(f"\n\nVisualização clientes cadastrados (TEMPORÁRIO)!\n{v_clientes}\n\n", p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)

    elif v_opcao_menu == "5":
        v_contas.append(fc_operacao_criar_conta(p_lst_clientes=v_clientes, p_gerador_sequence=v_gerador_sequence))
        # Visualizar Contas cadastradas. Solução temporária apenas para testes. Futuramente implementar funcionalidade no menu.
        fc_mensagem_temporizada(f"\n\nVisualização contas cadastradas (TEMPORÁRIO)!\n{v_contas}\n\n", p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)

    else:
        fc_mensagem_temporizada(p_mensagem="Opção inválida!\nFavor escolher uma das opções numéricas apresentada no menu.",
                                p_tempo_em_segundos=C_NUM_SEGUNDOS_TEMPORIZADOR)
        continue
        print("Opção inválida!\nFavor escolher uma das opções numéricas apresentada no menu.")
