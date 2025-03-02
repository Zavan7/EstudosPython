from openpyxl import load_workbook
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'Alunos.xlsx'

arquivo = load_workbook(CAMINHO_ARQUIVO)


aba_alunos = arquivo['Alunos']
print(aba_alunos)

print (aba_alunos['A2'].value)


