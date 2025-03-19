import functools   # Importante para a introspecção

# Decorador
def meu_decorador(funcao):
    @functools.wraps(funcao)   # Importante para a introspecção
    def envelope(*args, **kwargs):
        retorno_da_funcao = funcao(*args, **kwargs)
        return retorno_da_funcao
    
    return envelope

# Função ola_mundo DECORADA
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo! Meu nome é {nome}!")
    return nome.upper(), outro_argumento

# *** Programa Principal
retorno_maiusculo = ola_mundo("Jacinto Ventura", 1000)
print(retorno_maiusculo)

print(ola_mundo.__name__)   # Importante para a introspecção
