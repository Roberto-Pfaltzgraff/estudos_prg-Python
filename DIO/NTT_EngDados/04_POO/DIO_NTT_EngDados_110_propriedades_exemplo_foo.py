# Entendendo como funciona property() no Python

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    # Aplicando o @property para definir o método x() como uma propriedade/atributo
    # implicitamente já é o getter
    def x(self):
        return self._x or 0

    @x.setter
    # Aplicando o método setter, para definir o que fazer quando
    # houver uma atribuição para a propriedade do objeto
    def x(self, valor):
        # No setter e deleter não se usa retorna, apenas os comandos do que se deve fazer
        self._x += valor # Neste exemplo, estamos apenas adicionado o valor atribuido ao valor do atributo _x

    @x.deleter
    # Aplicando o método deleter, para definir o que fazer quando
    # houver uma deleção da propriedade do objeto
    def x(self):
        # No setter e deleter não se usa retorna, apenas os comandos do que se deve fazer
        self._x -= 1  # Neste exemplo, estamos apenas decrementando 1 do valor do atributo _x
        # A ação normal para esta ação seria:
        # del self._x

# Testando o @property e getter()
foo = Foo(10)
print(foo.x)

# Testando o setter()
foo.x = 30
print(foo.x)

# Testando o deleter()
del foo.x
print(foo.x)
