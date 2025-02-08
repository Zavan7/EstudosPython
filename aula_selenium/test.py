import json

arquivo_csv = 'desafio_2.json'

def open_json(arquivo_csv):

    with open (arquivo_csv, 'r', encoding= 'utf8') as f:
        dados = json.load(f)
        print(dados)

open_json(arquivo_csv)