# Nome do programa: tempo_laco_python.py
# Objetivo: Testar tempo para percorrer laço.
# Como?: Executando este código pela linha de comando (CMD),
# já tendo o prompt configurado com $p$b$t$g
# para obter hora, minuto, segundo e centesimos,
# antes e depois. Para ter uma ideia.
# Ficou assim: C:\Geral|12:56:26,10>python tempo_laco_python.py

QTD_REPETE_1SEGUNDO = 10000000
MAX_REPETE = QTD_REPETE_1SEGUNDO * 15
qtd_teste = 0
for temporizador in range(MAX_REPETE):
    qtd_teste = temporizador
print(qtd_teste)

# Resultado alcançado com esse teste:
# C:\Geral|13:07:33,61>
# C:\Geral|13:08:15,86>python tempo_laco_python.py
# 149999999
# 
# C:\Geral|13:08:21,36>