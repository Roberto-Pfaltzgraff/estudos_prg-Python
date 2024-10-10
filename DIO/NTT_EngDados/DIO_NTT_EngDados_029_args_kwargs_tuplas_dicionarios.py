def exibir_poema(data_extenso, *args, **kwargs):
# def exibir_poema(data_extenso, *tupla, **dicionario): # Poderia ser outro nome sem ser args e kwargs
    texto = "\n".join(args)
#    texto = "\n".join(tupla)  # Poderia ser outro nome sem ser args e kwargs
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
#    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])  # Poderia ser outro nome sem ser args e kwargs
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# Como o Python identificou a atribuição dos valores aos argumentos, uma vez que há somente 3 argumentos definidos?
# Sim, 3 argumentos definidos e vários atribuídos.
# data_extenso ⇒ é uma atribuição simples e singular, é um para um. Sem problemas de entender, pois é o 1º argumento e tudo se encaixa.
# args ⇒ Neste caso é uma tupla, pois foi usado * em sua definição, neste caso o Python espera receber uma lista de valores sequências do mesmo tipo, logo, ele considera todos os valores similares na sequência como pertencendo a essa estrutura de tupla, que consiste de 1 ou mais elementos do mesmo tipo, até encontrar o argumento com estrutura de dicionário, chave-valor. Então, ele para de considerar como sendo da tupla.
# kwargs ⇒ Inicia quando identifica um dicionário, uma lista de chave-valor e então vai até o final.

# Observe também que o último argumento encerra com virugla no final.

exibir_poema(
"RJ, terça-feira, 08 de outubro de 2024.",  # Corresponde ao argumento data_extenso
"Zen of Python",                            # Corresponde ao 1º elemento do argumento args
"Bonito é melhor que feio.",
"Explícito é melhor que implícito.",
"Simples é melhor que complexo.",
"Complexo é melhor que complicado.",
"Plano é melhor que aninhado.",
"Esparso é melhor que denso.",
"Legibilidade conta.",
"Casos especiais não são especiais o suficiente para quebrar as regras.",
"Embora a praticidade vença a pureza.",
"Erros nunca devem passar silenciosamente.",
"A menos que explicitamente silenciados.",
"Diante da ambiguidade, recuse a tentação de adivinhar.",
"Deve haver uma — e de preferência apenas uma — maneira óbvia de fazer isso.",
"Embora essa maneira possa não ser óbvia no início, a menos que você seja holandês.",
"Agora é melhor que nunca.",
"Embora nunca seja frequentemente melhor que *agora*.",
"Se a implementação for difícil de explicar, é uma má ideia.",
"Se a implementação for fácil de explicar, pode ser uma boa ideia.",
"Namespaces são uma ótima ideia -- vamos fazer mais disso!", # Corresponde ao último elemento do argumento args
autor="Tim Peters",                                # Corresponde ao 1º chave-valor do argumento kwargs
ano=1999,                                          # Corresponde ao último chave-valor do argumento kwargs
)