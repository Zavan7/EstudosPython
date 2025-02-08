# class A:
#     def __init__(self, nome):
#         self.x = 10
#         self.y = 20
#         self.nome = nome

#     def __str__(self):
#         parametros = ', '.join(
#             [f'{k}={v}' for k, v in self.__dict__.items()]
#         )
#         print(parametros)
#         return f'{self.__class__.__name__} - ({parametros})'

#     def __repr__(self):
#         return self.__str__()

# a= A('Vitor')

# print(a)

class StringMixin:
    def __str__(self):
        parametros = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        print(parametros)
        return f'{self.__class__.__name__} - ({parametros})'

    def __repr__(self):
        return self.__str__()

class MonoStateSiple(StringMixin):
    _state = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome and sobrenome is not None:
            self.nome = nome
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonoStateSiple('Vitor', 'Zavan')
    print(m1)