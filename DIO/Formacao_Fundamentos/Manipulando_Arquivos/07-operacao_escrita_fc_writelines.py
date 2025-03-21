# Abrindo um arquivo vazio para escrevê-lo
arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/teste_w.txt", "w")

# O método writelines() escreve uma lista ou qualquer iterável no arquivo, inserindo nele cada elemento
# Lembre-se que a string pode ser tratada como um iterável, por isso não há problema
# quando informamos apenas uma string e não uma lista
arquivo.writelines(["1-Essa eh", " a primeira frase"," ","escrita com writelines()1.", "\n", "Eita!", "   ", "Pulei linha no mesmo writelines"])
arquivo.writelines(["\n"])
arquivo.writelines("2-Essa eh a segunda frase escrita com writelines()2.")
arquivo.writelines("\n")
arquivo.write("Mesclando write() com os writelines(). Sem problemas.\n")

# Verificando se o write() aceita iterável como o writelines().
# Ele não aceita. Se descomentar o trecho abaixo, ocorre erro.
# Portanto essa é a diferença entre write() e writelines().
""" arquivo.write(["Testando write() recebendo iterável como o writelines().", " Sem problemas.", "\n"]) """

arquivo.writelines("3-Essa eh a terceira frase escrita com writelines()3.")

arquivo.close()
