# BootCamp DIO & NTT Data Engenharia de Dados com Python 🐍

## 🎯Objetivo:
Criar um sistema bancário com as operações: **sacar**, **depositar** e **visualizar extrato**.
O intuito é aplicar tudo que foi aprendido até essa etapa.
    ![alt text](img_DesafioAceito.png)

    
## 🤓Entendendo o Desafio:
>Fomos contratados por um grande banco para desenvolver seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem ***Python***.
Para a 1ª versão do sistema devemos implementar apenas **3 operações**: depósito, saque e extrato.
    


- 📋 1) Operação de depósito
    - Deve ser possível depositar **valores positivos** para minha conta bancária.
    - A versão v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
    - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato.
- 📋 2) Operação de saque
    - O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
    - Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
    - Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.
- 📋 3) Operação de extrato
    - Essa operação deve listar todos os depósitos e saques realizados na conta.
    - No fim da listagem deve ser exibido o saldo atual da conta.
    - Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
    Exemplo: 1500.45 ⇒ deve ser apresentado = R$ 1500.45.

- 🗺️Template do código (Mostrado no Desafio)
    
    ```python
    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
    
        opcao = input(menu)
    
        if opcao == "d":
            print("Depósito")
    
        elif opcao == "s":
            print("Saque")
    
        elif opcao == "e":
            print("Extrato")
    
        elif opcao == "q":
            break
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    ```

## 🤓Desafio Feito😎! Minha resolução🎉🎉🎉:
> Veja a solução do código no meu git:  
> 📋[DIO_NTT_EngDados_DESAFIO_01_criando_sistema_bancario.py](https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/DIO_NTT_EngDados_DESAFIO_01_criando_sistema_bancario.py)