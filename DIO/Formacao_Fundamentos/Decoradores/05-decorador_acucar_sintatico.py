# Decorador
def meu_decorador(funcao):
    def envelope():
        print("*** Faz algo antes ***")
        funcao()
        print("*** Faz algo depois ***")
    
    # Esse return pelo que entendi é o return do DECORADOR, neste caso do meu_decorador()
    return envelope

# Função ola_mundo DECORADA
@meu_decorador
def ola_mundo():
    print("Olá mundo!")

# *** Programa Principal
ola_mundo()