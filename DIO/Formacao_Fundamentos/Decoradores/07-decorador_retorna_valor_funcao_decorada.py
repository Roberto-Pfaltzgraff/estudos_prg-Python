# Decorador
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("*** Faz algo antes ***")
        retorno_da_funcao = funcao(*args, **kwargs)
        print("*** Faz algo depois ***")
        return retorno_da_funcao
    
    # Esse return pelo que entendi é o return do DECORADOR, neste caso do meu_decorador()
    return envelope

# Função ola_mundo DECORADA
@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! Meu nome é {nome}!")
    return nome.upper()

# *** Programa Principal
retorno_maiusculo = ola_mundo("Jacinto Ventura")
print(retorno_maiusculo)