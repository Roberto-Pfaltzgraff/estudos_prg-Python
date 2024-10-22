class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def saldo(self):
        return self._saldo


conta = Conta(100)
# O Python não faz a proteção do acesso a variável do objeto.
# Lembre: O underline é uma conveção amplamente usada na comunicadade, embora não garanta
# que algo como os comandos abaixo possam ser feitos, mas pela convenção não deveriam serem feitos.
conta._saldo += 1
print(conta._saldo)

# E como deveria serem feitos seguindo a convenção da comunidade de Python:
conta.depositar(1)
print(conta.saldo())
