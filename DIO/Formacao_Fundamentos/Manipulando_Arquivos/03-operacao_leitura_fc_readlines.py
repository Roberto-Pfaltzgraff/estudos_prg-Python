arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/lorem.txt", "r")
# Esse método readlines() lê o arquivo e retorna em uma lista,
# onde cada elemento é uma string referente a cada linha do arquivo.
for leitura in arquivo.readlines():
    print(leitura)

# Ou podemos substituir o For Readlines por esse trecho
# e ver o objeto lista com todos os elementos
# OBS: Se descomentar esse trecho, comente o trecho do For
""" leitura = arquivo.readlines()
print(leitura) """

arquivo.close()
