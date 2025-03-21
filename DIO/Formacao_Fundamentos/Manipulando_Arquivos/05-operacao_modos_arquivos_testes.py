# Modo de abertura de arquivo: r
# Ao abrir o arquivo nesse modo, ele precisa existir, caso contrario ocorre erro.
# Basta descomentar o código abaixo para ocorrer erro. Depois aponte para um arquivo existente.
""" arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/teste_r.txt", "r")
arquivo.close() """

# Modo de abertura de arquivo: w
# Se o arquivo não existir, ele será criado.
# Se o arquvo existir, todo seu conteúdo será descartado, será aberto como se tivesse criado vazio.
arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/teste_w.txt", "w")
arquivo.close()

# Modo de abertura de arquivo: a
# Se o arquivo não existir, ele será criado.
# Se o arquvo existir, todo seu conteúdo será mantido, e as novas escritas serão feitas no fim do arquivo.
arquivo = open("./DIO/Formacao_Fundamentos/Manipulando_Arquivos/teste_a.txt", "a")
arquivo.close()
