# Módulo: pytz (acronimo=PYthon Time Zone). Trabalhando com fusos horários em datas e horas
# antes de realizar o import, é necessário instalar o módulo/biblioteca pytz, caso não tenha feito.
# Comando a executar na linha de comando do prompt:
# pip install pytz
# Caso ocorra problema, siga esses comandos na linha de comando do prompt:
# python -m venv .env
# source .env/bin/ativate
# pip install pytz
from datetime import datetime

import pytz

# Como saber o valor da string a colocar no parâmetro do Time Zone?
# 1) Podemos consultar diretamente da lista do objeto/módulo/biblioteca pytz
# para isso basta fazer o seguinte, pode ser pelo interpretador Python no modo interativo:
# >>> import pytz
# >>> pytz.all_timezones
# >>> # Sitaxe: [nome for nome in pytz.all_timezones if "VALOR_DESEJADO" in nome]
# >>> [nome for nome in pytz.all_timezones if "Brazil" in nome]
# >>> [nome for nome in pytz.all_timezones if "Paulo" in nome]
# 2) Ou podemos descobrir consultando a lista de TIMEZONE em sites:
# https://en.wikipedia.org/wiki/List_of_time_zones_by_country
# https://en.wikipedia.org/wiki/Time_zone
# https://time.is/pt_br/UTC

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

print(type(data))
print(type(data2))