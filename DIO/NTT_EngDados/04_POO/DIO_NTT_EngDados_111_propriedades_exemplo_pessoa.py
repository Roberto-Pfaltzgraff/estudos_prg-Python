class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024 # O ano atual está hardcode, só para fins didáticos e foco no estudo de propriedades
        return _ano_atual - self._ano_nascimento
    

# main
pessoa = Pessoa("Noemi", 1962)
print(pessoa.nome, pessoa.idade, "anos")
