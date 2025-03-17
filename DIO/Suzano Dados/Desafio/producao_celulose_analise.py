def calcular_producao():
    # Entrada de dados do usuário
    # Valor para o teste:
    # Norte: 150.5, Sul: 200.0, Leste: 175.8, Oeste: 160.2
    entrada = input()

    # Separando as entradas de cada região e produção
    regioes_producao = entrada.split(', ')

    # TODO: Crie as variáveis para armazenar a produção total e o número de regiões
    total_producao = float(0)
    media_producao = float(0)
    qtd_regioes = 0

    # TODO: Itere sobre cada entrada de região: produção
    for regiao_producao in regioes_producao:
        # TODO: Divida a região e produção com base no caractere ":"
        regiao, producao = regiao_producao.split(": ")
        
        # TODO: Converta a produção para float e somando ao total
        producao = float(producao)
        total_producao = total_producao + producao
        qtd_regioes = qtd_regioes + 1
       

    # TODO: Calcule a média de produção por região
    media_producao = total_producao / qtd_regioes

    # Exibindo a produção total e média formatada
    print(f"Produção total: {total_producao:.2f} toneladas")
    print(f"Média por região: {media_producao:.2f} toneladas")

# Executa a função
calcular_producao()