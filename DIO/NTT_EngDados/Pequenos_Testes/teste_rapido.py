def filtrar_funcionarios(funcionarios, cargo):
    # TODO: Filtre os funcionários pelo cargo especificado
    listaNomesFiltrados = []
    for funcionario in funcionarios:
        if funcionario['cargo'] == cargo:
            listaNomesFiltrados.append(funcionario['nome'])
    return listaNomesFiltrados

# Função para entrada do usuário
def main_filtro():
    n = int(input("Digite um valor: "))
    funcionarios = []

    for _ in range(n):
        id_funcionario = int(input())
        nome = input()
        cargo = input()
        funcionarios.append({"id": id_funcionario, "nome": nome, "cargo": cargo})

    cargo_filtro = input()
    resultado = filtrar_funcionarios(funcionarios, cargo_filtro)
    
    print(resultado)

# Executando a função
main_filtro()