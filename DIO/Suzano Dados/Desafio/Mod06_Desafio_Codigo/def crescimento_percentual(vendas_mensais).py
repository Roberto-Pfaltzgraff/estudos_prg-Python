def crescimento_percentual(vendas_mensais):
    # TODO: Extraia os valores de venda de dois meses:
    mes1 = vendas_mensais[0]["valor_venda"]
    mes2 = vendas_mensais[1]["valor_venda"]
    
    # TODO: Calcule o crescimento percentual
    crescimento_percentual = (mes2 - mes1) / (mes1 + mes2) * 100
    return crescimento_percentual

vendas_mensais = []

for i in range(2):
    mes = input()
    valor_venda = float(input())
    vendas_mensais.append({"mes": mes, "valor_venda": valor_venda})

# TODO: Chame a função e imprime o resultado:
crescimento_percentual(vendas_mensais)
print(f"Crescimento percentual de vendas: {resultado:.2f}%")