from datetime import timedelta, date, time, datetime

# ********* Meus teste *********
# Para entender os tipos e valores com operações de data e hora
delta = timedelta(seconds=1)
print(delta)

# Verificar tipos
v_data = date.today() # Valor de date
v_timedelta = timedelta(days=1, hours=6, minutes=30, seconds=10) # Valor timedelta representa duração de tempo
print(type(v_data))
print(type(v_timedelta))
print(v_data)
print(v_timedelta)
v_data_ini = date(2024, 10, 20) # Valor data inicio tipo date 20/10/2024
v_data_fim = date(2024, 10, 21) # Valor data final tipo date 21/10/2024
v_diferenca = v_data_fim - v_data_ini  # Quero identificar se o tipo da operação de diferença é uma duração do tipo timedelta
print(type(v_diferenca))   # Confirmado que a operação de diferença entre datas é um timedelta
print(v_diferenca)         # e o respectivo valor da diferença
#
# Ocorre erro quando se realiza operação de soma
# informando valor date em ambos operadores
# basta descomentar a linha abaixo.
'''v_soma_data = v_data_ini + v_data_fim'''
#
# Entretanto, operação de soma entre um date e um timedelta funciona
v_soma_data_1 = v_data_ini + v_diferenca
v_soma_data_2 = v_diferenca + v_data_ini
print(v_soma_data_1)
print(v_soma_data_2)


# ********* Exemplo da Trilha Python do BootCamp *********
'''Aqui ele simula um sistema para um lava-jato poder
calcular a data hora de entrega do carro.'''
# from datetime import date, datetime, timedelta # já definido por mim, mas acima

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

# print(time(10, 19, 20) - timedelta(hours=1)) # Erroooooooooooooooooo
# Esse comando de cima dá erroooooooo
# pois não suporta a operação => time() - deltatime()
# para funcionar tem que fazer o artificio abaixooooooooo
# usando a operação com datetime() em vez do time() direto
# coloca uma data qq com a hora a ser trabalhada.
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())  # E aqui consegue pegar a hora decrementada

print(datetime.now().date()) # Também é possível obter apenas a data