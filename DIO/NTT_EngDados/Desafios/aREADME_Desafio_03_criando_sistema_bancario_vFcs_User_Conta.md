# BootCamp DIO & NTT Data Engenharia de Dados com Python 🐍 (*Desafio 03*)

## 🎯Objetivo:
Alterar o sistema bancário, criado anteriormente nos desafios, para implementar novas funcionalidades, transformando as operações já implementadas em funções e criando as novas operações de cadastro de usuário e contas já como funções.  
  
O intuito é aplicar tudo que foi aprendido até essa etapa.  
  
![alt text](img_DesafioAceito.png)


## 🤓Entendendo o Desafio:
>Após desenvolvermos o sistema bancário para um grande banco.  
Esse banco deseja avançar com a modernizar, implementando novas funcionalidades.  
Precisamos deixar nosso código mais modularizado.  
Será a oportunidades de aplicarmos o conhecimento adquirido no Python sobre funções.
    


- 📋 1) Transformar as codificações das operações em funções ✅🆗(Já implementado desta forma na etapa 1)
    - Cada operação precisa ser codificada como função.✅(Já tinha feito desta forma)
    - A os argumentos das funções deve seguir a seguinte ordem:
        - Função da operação **Saque** deve conter os argumentos apenas por nome (keyword only).
        - Função da operação **Depósito** deve conter os argumentos apenas por posição (positional only).
        - Função da operação **Extrato** deve conter os argumentos por posição e nome (positional only e keyword only). Sendo o argumento _saldo_ por posição e o argumento _extrato_ por nome.
- 📋 2) Criar a função de Cadastrar Usuário (Cliente do banco)
    - O sistema deve armazenar os usuários em uma lista.
    - Um usuário é composto por: nome, data nascimento, cpf e endereço.
    - O endereço é uma string com o formato: logradouro, número - bairro - cidade - sigla do estado.
    - CPF deve conter apenas números.
    - Não pode haver mais de 1 usuário com o mesmo CPF.
- 📋 3) Criar a função de Cadastrar Conta Bancária (vincular com o Usuário/Cliente)
    - O sistema deve armazenar as contas em uma lista.
    - Uma conta é composta por: agência, número da conta e usuário.
    - O número da conta é um sequencial, iniciado em 1.
    - O número da agência é fixo: "0001"
    - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.  
  
- 🗺️Template do código (Desafio 3)  
Vou implementar o código para esse Desafio 3, considerando como ponto de partida:  
     - O template do Desafio 2, o último que fiz, e consta no GitHub:  
     [DIO_NTT_EngDados_DESAFIO_02_criando_sistema_bancario_vData.py](https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/DIO_NTT_EngDados_DESAFIO_02_criando_sistema_bancario_vData.py)  


## 🤓Desafio Feito😎! Minha resolução🎉🎉🎉:
> Veja a solução no código do meu git:  
> 📋- [DIO_NTT_EngDados_DESAFIO_03_criando_sistema_bancario_vFcs_User_Conta.py](https://github.com/Roberto-Pfaltzgraff/estudos_prg-Python/blob/main/DIO/NTT_EngDados/Desafios/DIO_NTT_EngDados_DESAFIO_03_criando_sistema_bancario_vFcs_User_Conta.py)  
  
