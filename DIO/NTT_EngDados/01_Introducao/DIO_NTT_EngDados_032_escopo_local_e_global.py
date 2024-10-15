salario = 2000
lista = [1, 2] # É um objeto imutável. Logo, ela é poderá ser utilizada em qualquer escopo sem ter que referenciar como global

def salario_bonus(bonus):
    global salario  # Comente esta linha e execute para confirmar que o Python não reconhece uma variável global sem que seja especificado por global
    lista.append(3) # Consigo referenciar e chamar seu método sem ter que informar como global
    salario += bonus
    return salario

print(salario_bonus(500))
print(salario)
print(lista)

