import pandas as pd
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent.parent/ 'dados2.xlsx'
df = pd.read_excel(CAMINHO_ARQUIVO)

print(df)