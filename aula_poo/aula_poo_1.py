# atributo = dentro da classe
# metodo da classe, são as funções

import json
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula_poo.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Vitor', 20)
p2 = Pessoa('João', 30)
p3 = Pessoa('Maria', 40)
p4 = Pessoa('Eustacio', 35)
p5 = Pessoa ('Genoveva', 29)
bd = [vars(p) for p in [p1, p2, p3, p4, p5]]

def dump():
    with open(CAMINHO_ARQUIVO, 'w') as f:
        json.dump(bd, f, ensure_ascii=False, indent=2)
        print('Sucess')

if __name__ == '__main__':
    dump()