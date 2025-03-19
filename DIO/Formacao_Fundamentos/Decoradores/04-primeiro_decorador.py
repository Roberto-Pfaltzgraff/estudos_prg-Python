# Decorador
def meu_decorador(funcao):
    def envelope():
        print("*** Faz algo antes ***")
        funcao()
        print("*** Faz algo depois ***")
    
    # Esse return pelo que entendi é o return do DECORADOR, neste caso do meu_decorador()
    return envelope

# Função ola_mundo
def ola_mundo():
    print("Olá mundo!")

# *** Programa Principal
print("$$$ Sem uso do Decorador")
ola_mundo()

print("$$$ Com uso do Decorador")
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
