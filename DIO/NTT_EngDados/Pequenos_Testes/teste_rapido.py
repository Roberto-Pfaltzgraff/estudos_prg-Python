class Cliente:
    def __init__(self, enderenco):
        self._endereco = "Rua" #enderenco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__("Rua")

def menu():
    C_MENU = """\n
        *************** MENU ***************

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Cadastrar Usuário/Cliente
        [5] Criar Conta Corrente
        [0] Sair

        Digite o número correspondente a opção desejada: """
    return input(C_MENU.replace(" " * 8, ""))

def main():
    op = menu()
    return True


# *** Programa Principal (POO) ***
main()

a = PessoaFisica(1, "Roberto", 12)
print(a._nome)
print(a._endereco)
print(a._cpf)
print(a._contas)
print(a._data_nascimento)