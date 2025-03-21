from pathlib import Path
ROOT_PATH = Path(__file__).parent
print("*"*50)
print(ROOT_PATH)
print("#"*50)

# Exceção: FileNotFoundError
try:
    arquivo = open("arquivo_xyz.txt")
except FileNotFoundError as detalhe_excecao:
    print("Arquivo não existente!\nErro recebido do S.O.:")
    print(detalhe_excecao)

# Exceção: IsADirectoryError    *** OBS: que Manipulando_Arquivos é um diretório e não arquivo.
try:
    arquivo = open(ROOT_PATH, "r")
except IsADirectoryError as detalhe_excecao:
    print(f"Erro ao abrir o arquivo. Pode ser um diretório em vez de arquivo. Veja erro do S.O.:\n{detalhe_excecao}.")
except PermissionError as detalhe_excecao:
    print(f"{"*"*50}\nErro de PERMISSÃO. Acabou caíndo aqui. Veja erro do S.O.:\n{detalhe_excecao}.\n{"*"*50}")
