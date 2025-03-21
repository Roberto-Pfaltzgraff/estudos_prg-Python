# Dica para tratar Arquivos Grandes sem precisar de Geradores e gerenciando bem memória
arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/lorem.txt", "r")

# Lógica dessa Dica: O laço While é executado até o fim do arquivo lendo uma linha por vez.
# A atribuição de cada leitura é feita do readline() para o objeto leitura, através do operador Morsa*,
# e a função len() faz a contagem da quantidade de caracteres de cada linha por meio do objeto leitura.
# Enquanto não for final de arquivo, o valor de len() será diferente de zero,
# o que para o Python significa VERDADEIRO. E quando for zero será FALSO, o que ocorrerá apenas
# quando chegar no final do arquivo.
while len(leitura := arquivo.readline()):
    print(leitura)
# * Operador Morsa ":=". Ele foi introduzido no Python 3.8
# e serve para atribuir um valor a uma variável dentro de uma expressão.

arquivo.close()
