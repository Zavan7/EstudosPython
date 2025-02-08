import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'ex.csv'

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
    
#     for i in leitor:
#         print(i)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for i in leitor:
        print(i['Nome'], i['Sobrenome'], i['Idade'])