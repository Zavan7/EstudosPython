class Meta(type):
    def __call__ (cls, *arg, **kwargs):
        return super().__call__(*arg, **kwargs)

class Pessoa(metaclass=Meta):
    def __new__(cls, *arg, **kwargs):
        return super().__new__(cls)

    def __init__(self, nome):
        self.nome = nome

    def __call__ (self):
        print('Call chamado')

p1 = Pessoa('Vitor')
p1()
print(p1.nome)