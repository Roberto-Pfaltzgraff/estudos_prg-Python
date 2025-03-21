arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/lorem.txt", "r")
# Esse método read() lê o arquivo todo e o retorna em uma única string
leitura = arquivo.read()
arquivo.close()
print(leitura)
