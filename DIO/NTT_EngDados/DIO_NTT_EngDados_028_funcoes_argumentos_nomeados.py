def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados ...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Mudando a ordem, temos problemas com os valores esperados.
# Podendo causar erro ou atribuição indevida
salvar_carro(1999, "ABC-1234", "Fiat", "Palio")

# Fazendo a mesma mudança de ordem dos argumentos, não há problemas quando o mesmo é nomeado
salvar_carro(ano=1999, placa="ABC-1234", marca="Fiat", modelo="Palio")

# Fazendo a mesma mudança de ordem dos argumentos, não há problemas quando o mesmo é dicionário
salvar_carro(**{"ano": 1999, "placa": "ABC-1234", "marca": "Fiat", "modelo": "Palio"})
