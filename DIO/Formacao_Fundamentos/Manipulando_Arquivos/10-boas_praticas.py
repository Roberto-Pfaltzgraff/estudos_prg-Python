from pathlib import Path
ROOT_PATH = Path(__file__).parent

# Boa Prática >> Abrir arquivos com gerenciador de contexto: with.
# Isso garante que tudo seja fechado ao encerrar o with.
with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
    print(arquivo.read())

print("Fora do with o <<arquivo>> já não existem mais!")

# Boa Prática >> Garantir que o arquivo foi aberto corretamente antes de iniciar o processamento.
try:
    with open(ROOT_PATH / "xpto_xyz.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir arquivo!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")

# Boa Prática >> Usar a codificação de arquivo correta.
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="UTF-8") as arquivo:
        arquivo.write("Aprendendo boas práticas em manipulação de arquivos com Python!")
except IOError as exc:
    print(f"Erro ao criar/abrir o arquivo!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")
print("Fim do processo de criação do arquivo UTF-8.")

# Fazendo um teste na leitura desse arquivo com um enconde diferente
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao tentar ler o arquivo!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")
except UnicodeDecodeError as exc:
    print(f"Erro de Decodificação do UNICODE!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")
except Exception as exc:
    print(f"Erro Geral!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")

# Fazendo um teste na leitura desse arquivo com o enconde correto
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="UTF-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao tentar ler o arquivo!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")
except UnicodeDecodeError as exc:
    print(f"Erro de Decodificação do UNICODE!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")
except Exception as exc:
    print(f"Erro Geral!\nRetorno:\n{"*"*50}\n{exc}\n{"*"*50}")