def exibir_mensagem_1():
    print("MSG1 | Minha primeira função em Python!")

def exibir_mensagem_2(nome):
    print(f"MSG2 | O nome recebido no parâmetro é {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"MSG3 | O nome recebido no parâmetro é {nome}!")
    print("OBS: Se for Anônimo é porque o valor do parâmetro não foi informado na chamada da função.")

def exibir_mensagem_4(numero=0.00):
    print(f"MSG4 | O numero recebido no parâmetro é {numero:.2f}!")


exibir_mensagem_1()
# exibir_mensagem_2() # Aqui ocorre erro porque o parametro é obrigatório, uma vez que a função não definiu o parâmetro com valor default.
exibir_mensagem_2(nome="Roberto Primeiro")
exibir_mensagem_3()
exibir_mensagem_3(nome="Roberto Segundo")
exibir_mensagem_3("Roberto Segundo .5") # Assim, apenas com o valor do parêmetro e sem o nome, também funciona!
exibir_mensagem_4()
exibir_mensagem_4(numero=125.254687)
exibir_mensagem_4(1250) # Assim, apenas com o valor do parêmetro e sem o nome, também funciona!