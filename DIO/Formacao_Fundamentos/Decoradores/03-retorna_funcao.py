def fc_calculadora(operacao):
    def fc_soma(a, b):
        return a + b
    
    def fc_subtracao(a, b):
        return a + b
    
    def fc_multiplicacao(a, b):
        return a + b
    
    def fc_divisao(a, b):
        return a + b
    
    match(operacao):
        case "+":
            return fc_soma
        case "-":
            return fc_subtracao
        case "*":
            return fc_multiplicacao
        case "/":
            return fc_divisao

# Programa Principal

# Uma forma de chama a função que retorna função (Atenção na Passagem de parametros)
print(fc_calculadora("+")(2, 3))

# Outra forma de chama a função que retorna função (Atenção na Passagem de parametros)
operacao = fc_calculadora("+")
print(operacao(5,7))