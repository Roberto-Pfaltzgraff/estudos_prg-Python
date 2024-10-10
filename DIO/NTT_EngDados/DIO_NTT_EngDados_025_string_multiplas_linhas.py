nome = "Roberto"

mensagem_1_com_aspas_simples = '''
Olá, meu nome é Roberto.
     Estou aprendendo Python.
  Neste momento, strings com multiplas linhas.'''

mensagem_2_com_aspas_duplas = """
Olá, meu nome é Roberto. Está é a 2ª mensagem e com aspas duplas.
     Estou aprendendo Python.
  Neste momento, strings com multiplas linhas."""

mensagem_3_com_aspas_e_interpolacao = f"""
Olá, meu nome é {nome}. Está é a 3ª mensagem com aspas duplas e interpolação f-string.
     Estou aprendendo Python.
  Neste momento, strings com multiplas linhas."""

print("Mensagem_1")
print(mensagem_1_com_aspas_simples)
print("Mensagem_2")
print(mensagem_2_com_aspas_duplas)
print("Mensagem_3")
print(mensagem_3_com_aspas_e_interpolacao)
print("FIM")

print(
    """
    =============== MENU ===============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ====================================

             Obrigado por usar nosso sistema!
    """
)