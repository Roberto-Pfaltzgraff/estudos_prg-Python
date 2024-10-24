# Desafio do BootCamp DIO & NTT Data Engenharia de Dados com Python (Desafio 4 - POO)
# Objetivo do 4º Desafio - POO: 
#     Alterar o sistema bancário, criado anteriormente nos desafios,
#     para iniciar a modelagem do sistema bancário em POO.
#     Adicionar classes para cliente.
#     E passar para classes as operações bancárias existentes: depósito e saque.
#     O intuito é aplicar tudo que foi aprendido até essa etapa.
# Ponto de Partida (Código que fiz no 3º Desafio):
#     https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/DIO_NTT_EngDados_DESAFIO_03_criando_sistema_bancario_vFcs_User_Conta.py
#     https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/aREADME_Desafio_03_criando_sistema_bancario_vFcs_User_Conta.md

# *** Módulos necessários ***
from datetime import datetime, date, time, timedelta # Por enquanto sem necessidade: , timezone
from abc import ABC, abstractmethod, abstractproperty

# Definição das Classes
class Cliente:
    def __init__(self, enderenco):
        self._endereco = enderenco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    def __str__(self):
        # Quis implementar a listagem de clientes e achei melhor pegar essa ideia do ContaCorrente
        return f"\nCPF: {self._cpf}\nNome: {self._nome}\nData Nascimento: {self._data_nascimento}\nEndereço: {self._endereco}\n"
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self._saldo = 0
        self._historico = Historico()
        self._numero = numero
        self._agencia = "0001" # agencia , FIXME: Futuramente quando tiver outras agencias, já temos o parametro
        self._cliente = cliente
    
    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        # Verdade! Aqui faz todo sentido ser Método de Classe,
        # pois não preciso ter um objeto Conta instanciado para acionar
        # este que irá criar uma conta chamando o construtor dela mesmo.
        return cls(cliente, numero)
    
    # Não havia pensado na definição dos outros properties. Segue:
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        # TODO: Implementar demais regras / controles / criticas de movimentos. Já feitos: limites e saldos.
        operacao_validada = ( (valor > 0) and (valor <= self.saldo) )
        if operacao_validada:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Falha na operação de saque!\n<VALOR INVÁLIDO ou NÃO HÁ SALDO!>")
        return operacao_validada
    
    def depositar(self, valor):
        # TODO: Implementar demais regras / controles / criticas de movimentos. Já feitos: limites e saldos.
        operacao_validada = (valor > 0)
        if operacao_validada:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Falha na operação de depósito!")
        return operacao_validada

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia="0001", limite_valor=500, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self._limite_valor = limite_valor
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        # Extendendo o Método p/ Adicionar tratamentos de limites
        # TODO: Considerar data. Pois os limites de saque, valor e transações são diários
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite_valor = valor > self._limite_valor
        excedeu_limite_saque = numero_saques >= self._limite_saques

        if excedeu_limite_valor:
            print("Falha na operação de saque!\n<O VALOR LIMITE FOI EXCEDIDO!>")
        
        elif excedeu_limite_saque:
            print("Falha na operação de saque!\n<A QUANTIDADE DE SAQUES DIÁRIO FOI EXCEDIDA!>")
        else:
            # Até aqui adicionamos funcionalidades no método extendido
            # na próxima linha, faremos tudo que já é feito no método base/pai
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        # Nem pensei em implementar esse método rsrs. Ajustei depois de ver a resolução.
        return f"\nAgência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente._nome}\n"

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractproperty
    def valor(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_operacao = conta.depositar(self.valor)
        
        if sucesso_operacao:
            conta.historico.adicionar_transacao(self)
        
class Saque(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_operacao = conta.sacar(self.valor)
        
        if sucesso_operacao:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


# Funções
def menu():
    C_MENU = """\n
        *************** MENU ***************

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Cadastrar Usuário/Cliente
        [5] Criar Conta Corrente
        [6] Listar Clientes
        [7] Listar Contas
        [0] Sair

        Digite o número correspondente a opção desejada: """
    return input(C_MENU.replace(" " * 8, ""))

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

def encontrar_cliente(cpf, clientes):
    clientes_encontrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_encontrados[0] if clientes_encontrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    
    # TODO: Implementar futuramente a escolha da conta
    return cliente.contas[0]

def fc_depositar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = fc_ler_valor_monetario("Informe o valor do depósito: R$ ")
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def fc_sacar(clientes):
    cpf = input("Informe o CPF: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = fc_ler_valor_monetario("Informe o valor do saque: R$ ")
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def fc_exibir_extrato(clientes):
    C_QTD_CARACTERES_EXTRATO = 70
    cpf = input("Informe o CPF: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    transacoes = conta.historico.transacoes

    # Impressão Extrato
    extrato = "Extrato Bancário".center(C_QTD_CARACTERES_EXTRATO, "=")  # Cabeçalho
    if not transacoes: # Conteúdo da movimentação
        extrato += "\nSua conta bancária não possui movimentações!"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["data"]} - {transacao['tipo']}: R$ {transacao['valor']:.2f}"

    extrato += ("\n" + ("-" * C_QTD_CARACTERES_EXTRATO))  # Separador
    extrato += f"\nSeu Saldo atual é de R$ {conta.saldo:.2f}." # Exibindo Saldo
    extrato += ("\n" + ("=" * C_QTD_CARACTERES_EXTRATO))  # Rodapé
    print(extrato)

def fc_criar_conta(clientes, contas, numero_conta):
    cpf = input("Informe o CPF: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("Conta criada com sucesso!")

def fc_cadastra_cliente(clientes):
    cpf = input("Informe o CPF: ")
    cliente = encontrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado com este CPF!")
        return
    
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Data de Nascimento (DD/MM/YYYY): ")
    endereco = input("Endereço (Logradouro, número - Bairro - Cidade - UF): ")

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")

# def fc_listar_clientes(clientes):
#     for cliente in clientes:
#         print(f"{'=' * 70}\n{str(cliente)}\n")
#
# def fc_lisar_contas(contas):
#     for conta in contas:
#         print(f"{'=' * 70}\n{str(conta)}\n")
#
# Simplificando os 2 métodos anteriores apenas nesse
# que servirá tanto para listar os clientes quanto as contas cadastradas
def fc_listar_objetos(lista_objetos):
    for objeto in lista_objetos:
        print(f"{'=' * 70}\n{str(objeto)}\n")

def fc_sequence_conta():
    # Função similar a uma sequence de banco para gerar o número sequencial
    # da conta bancária, começando em 1.
    v_sequencia = 0
    while True:
        v_sequencia += 1
        yield v_sequencia

def fc_modo_teste(modo_teste, clientes, contas, p_sequence_numero_conta):
    if modo_teste:
        # Inicializar com Cliente e Conta cadastrados
        cliente = PessoaFisica(cpf="1", nome="Juca Silva", data_nascimento="15/06/1998", endereco="Rua A, 1 - Centro - Carnuiba - MT")
        clientes.append(cliente)

        numero_conta = next(p_sequence_numero_conta)
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.adicionar_conta(conta)

def main():
    clientes = []
    contas = []
    v_sequence_numero_conta = fc_sequence_conta()
    # NOTE: Essa função foi para automatizar um pouco os testes.
    # ao final dos testes, devemos mudar o 1o argumento para FALSE.
    fc_modo_teste(modo_teste=True, clientes=clientes, contas=contas, p_sequence_numero_conta=v_sequence_numero_conta)
    while True:
        # Laço de interação do Menu
        opcao_menu = menu()

        if opcao_menu == "0":
            print("Obrigado por ser nosso cliente e utilizar nossos serviços!")
            break

        elif opcao_menu == "1":
            fc_depositar(clientes)
        
        elif opcao_menu == "2":
            fc_sacar(clientes)
        
        elif opcao_menu == "3":
            fc_exibir_extrato(clientes)
        
        elif opcao_menu == "4":
            fc_cadastra_cliente(clientes)

        elif opcao_menu == "5":
            numero_conta = next(v_sequence_numero_conta)
            fc_criar_conta(clientes, contas, numero_conta)

        elif opcao_menu == "6":
            # fc_listar_clientes(clientes) # FIXME: Substituindo por:
            fc_listar_objetos(clientes)

        elif opcao_menu == "7":
            # fc_lisar_contas(contas) # FIXME: Substituindo por:
            fc_listar_objetos(contas)

        else:
            print("Opção inválida!\nFavor escolher uma das opções numéricas apresentada no menu.")
            continue
    return True


# *** Programa Principal (POO) ***
main()
