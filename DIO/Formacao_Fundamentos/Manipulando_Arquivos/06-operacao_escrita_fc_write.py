# Abrindo um arquivo vazio para escrevê-lo
arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/teste_w.txt", "w")

# O método write() escreve uma string no arquivo
arquivo.write("1-Essa eh a primeira frase escrita com write()1.")
arquivo.write("\n")
arquivo.write("2-Essa eh a segunda frase escrita com write()2.")
arquivo.write("\n")
arquivo.write("3-Essa eh a terceira frase escrita com write()3.")

arquivo.close()
