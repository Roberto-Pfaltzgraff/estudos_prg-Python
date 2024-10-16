from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())

print()

data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())
print()
print(datetime(2025,12,15,13,27,30))
print(datetime(2025,12,15,13,27))
print(datetime(2025,12,15,13,27,30,125))

print()
hora = time(10, 20, 0)
print(hora)
print(time()) # 00:00:00
