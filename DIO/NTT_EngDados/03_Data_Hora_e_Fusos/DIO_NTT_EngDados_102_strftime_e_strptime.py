# Conhecendo strftime e strptime

# ******* Exemplo do curso:
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))


# ******* Meus testes:
v_datetime_now = datetime.now()
v_str_f_time = v_datetime_now.strftime("%d/%m/%Y %H:%M")
v_str_p_time = datetime.strptime("12/10/2024 10:20", "%d/%m/%Y %H:%M")
print(v_str_f_time)   # Retorno => 15/10/2024 19:10
print(v_str_p_time)   # Retorno => 2024-10-12 10:20:00
print(type(v_str_f_time))   # Retorno => <class 'str'>
print(type(v_str_p_time))   # Retorno => <class 'datetime.datetime'>
# Conclusão:
#    - O método strftime() retorna um objeto string => <class 'str'>
#    Logo, o strftime() converte Data/Hora ==em==> String
#    - O método strptime() retorna um objeto datetime => <class 'datetime.datetime'>
#    Logo, o strptime() converte String ==em==> Data/Hora