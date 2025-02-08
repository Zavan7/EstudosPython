from aula_poo_1 import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r') as f:
    dados = json.load(f)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    p4 = Pessoa(**dados[3])
    p5 = Pessoa(**dados[4])

    print(f'Nome: {p1.nome} - Idade: {p1.idade}')
    print(f'Nome: {p2.nome} - Idade: {p2.idade}')
    print(f'Nome: {p3.nome} - Idade: {p3.idade}')
    print(f'Nome: {p4.nome} - Idade: {p4.idade}')
    print(f'Nome: {p5.nome} - Idade: {p5.idade}')

