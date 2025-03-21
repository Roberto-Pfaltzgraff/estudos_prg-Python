import csv
from pathlib import Path
ROOT_PATH = Path(__file__).parent

# Escrita de um arquivo csv
try:
    # O parametro newline foi utilizado para que o arquivo gerado não ficasse com uma linha em branco entre os registros
    with open(ROOT_PATH / "usuarios.csv", "w", encoding="UTF-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Id", "Nome", "Data Nascimento"])
        escritor.writerow(["1", "Kelly", "16/06/1992"])
        escritor.writerow(["2", "Pedro", "31/10/1988"])
        escritor.writerow(["3", "Miriam", "27/03/1981"])
        escritor.writerow(["4", "Rafael", "01/08/1995"])
except IOError as exc:
    print(f"Erro ao Criar/Abrir o arquivo!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")
except Exception as exc:
    print(f"Erro Inesperado!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")

# Leitura de um arquivo csv
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="UTF-8", newline="") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except IOError as exc:
    print(f"Erro ao Criar/Abrir o arquivo!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")
except Exception as exc:
    print(f"Erro Inesperado!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")

# Leitura de um arquivo csv para um Dicionário com o método DictReader()
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="UTF-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        print(f"Fazendo leitura do csv para um Dicionário. E imprimindo:")
        for linha in leitor:
            print("Elementos desta linha:", linha["Id"], linha["Nome"], linha["Data Nascimento"])
            print(f"ou como Dicionário: {linha}")
except IOError as exc:
    print(f"Erro ao Criar/Abrir o arquivo!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")
except Exception as exc:
    print(f"Erro Inesperado!\n{"*"*50}\nErro Retornado:\n{exc}\n{"*"*50}")
