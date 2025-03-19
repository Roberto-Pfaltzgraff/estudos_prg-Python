# Decorador
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("*** Faz algo antes ***")
        funcao(*args, **kwargs)
        print("*** Faz algo depois ***")
    
    # Esse return pelo que entendi é o return do DECORADOR, neste caso do meu_decorador()
    return envelope

# Função ola_mundo DECORADA
@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! Meu nome é {nome}!")

# *** Programa Principal
ola_mundo("Jacinto Ventura")