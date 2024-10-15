# Definição da função para testar parêmtros especiais, com os recursos / e *
# Nessa definição:
# ano e placa ==> Foram definidos de modo que a passagem de parâmetros seja apenas por posição
# marca e modelo ==> Foram definidos de modo que a passagem de parâmetros seja hibrida, ou seja, por posição ou nome.
# pais e combustivel ==> Foram definidos de modo que a passagem de parâmetros seja apenas por nome
def criar_carro(ano, placa, /, marca, modelo, *, pais, combustivel):
    print(ano, placa, marca, modelo, pais, combustivel)


# A sequencia de comandos abaixo chamando a função, estão comentadas para que se possa testá-las.
# O ideal é descomentar uma de cada vez, executar e verificar o resultado e motivo para melhor entendimento
criar_carro(1999, "ABC-1234", "Fiat", "Argo", pais="Brasil", combustivel="Flex") # Valido
criar_carro(1999, "ABC-1234", "Fiat", "Argo", combustivel="Flex", pais="Brasil") # Valido
criar_carro(1999, "ABC-1234", marca="Fiat", modelo="Argo", pais="Brasil", combustivel="Flex") # Valido
criar_carro(1999, "ABC-1234", modelo="Argo", marca="Fiat", combustivel="Flex", pais="Brasil") # Valido
#criar_carro(ano=1999, placa="ABC-1234", marca="Fiat", modelo="Argo", pais="Brasil", combustivel="Flex") # Invalido (VSCode nem apresentou o nome do argumento)
#criar_carro(placa="ABC-1234", ano=1999, modelo="Argo", marca="Fiat", combustivel="Flex", pais="Brasil") # Invalido (VSCode nem apresentou o nome do argumento)
#criar_carro(1999, "ABC-1234", "Fiat", "Argo", "Brasil", "Flex") # Invalido
#criar_carro(1999, "ABC-1234", "Fiat", "Argo", "Flex", "Brasil") # Invalido
#criar_carro(1999, "ABC-1234", marca="Fiat", modelo="Argo", "Brasil", "Flex") # Invalido
#criar_carro(1999, "ABC-1234", modelo="Argo", marca="Fiat", "Flex", "Brasil") # Invalido