def fc_mensagem(nome):
    print("! Executando a função mensagem!")
    return f"Oi, {nome}!"

def fc_mensagem_longa(nome):
    print("! Executando a função mensagem_longaaaaaaaa!")
    return f"Espero que esteja tudo bem com você, {nome}!"

def fc_executar_msg(funcao, param):
    print("! Executando a função executa_mensagem!")
    return funcao(param)

print(fc_executar_msg(fc_mensagem, "Verônica"))
print(fc_executar_msg(fc_mensagem_longa, "Kelly"))