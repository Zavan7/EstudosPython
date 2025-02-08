from dataclasses import dataclass


@dataclass(init=False)
@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':

    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)