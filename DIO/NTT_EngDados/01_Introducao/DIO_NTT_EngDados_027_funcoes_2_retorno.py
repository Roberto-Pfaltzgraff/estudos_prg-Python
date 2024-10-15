def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
   
#    return antecessor, numero, sucessor   ### Comentando a linha debaixo e tirando deste, podemos ver que é possível retornar mais de 2 parâmetros
    return antecessor, sucessor


def func_sem_retorno_explicito():
    print("Executei a função. Há sempre um retorno da função, mesmo quando não é definido, por padrão retorna None implicitamente.")



print(calcular_total([10, 20, 34]))  # Resultado = 64
print(retorna_antecessor_e_sucessor(10))  # Resultado = (9, 11)
print(func_sem_retorno_explicito())  # Resultado = None