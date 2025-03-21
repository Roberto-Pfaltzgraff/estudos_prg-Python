import os
import shutil
from pathlib import Path

# __file__ é um atributo da classe que retorna o seu nome de arquivo com o caminho.
print(__file__)

# Obtendo o caminho do arquivo deste programa
ROOT_PATH = Path(__file__)
PRG_DIR = ROOT_PATH.parent
print("Diretório do programa eh:")
print(PRG_DIR)

# Obtendo o caminho do diretório corrente (Tive curiosidade e Pesquisei o Módulo p/ descobrir)
CUR_DIR = Path.cwd()
print("Diretório corrente eh:")
print(CUR_DIR)

# Criar Diretório
os.mkdir(PRG_DIR / "novo-diretorio")

# Copiando um arquivo
shutil.copy(PRG_DIR / "lorem.txt", PRG_DIR / "novo-diretorio")

# Renomear Arquivo
os.rename(PRG_DIR / "novo-diretorio" / "lorem.txt", PRG_DIR / "novo-diretorio" / "renomeado.txt")

# Mover um Arquivo
shutil.move(PRG_DIR / "novo-diretorio" / "renomeado.txt", PRG_DIR)

# Remover Arquivo e Diretório
os.remove(PRG_DIR / "renomeado.txt")
os.removedirs(PRG_DIR / "novo-diretorio")