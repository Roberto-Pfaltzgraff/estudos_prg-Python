arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/lorem.txt", "r")
# Esse método readline() lê uma linha do arquivo por vez e a retorna em uma string a cada fetch
leitura = arquivo.readline()
print(leitura)
leitura = arquivo.readline()
print(leitura)
leitura = arquivo.readline()
print(leitura)
arquivo.close()
