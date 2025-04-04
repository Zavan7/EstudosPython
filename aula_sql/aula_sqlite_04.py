import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'clientes'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

connection.commit()

cursor.execute(
     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
 )
connection.commit()

# Cria tabelas
cursor.execute(
    F'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'peso REAL'
    ')'
)
connection.commit()

# Registra valores nas colunas
# CUIDADO: sql injection
sql =(
    f'INSERT INTO {TABLE_NAME} '
    '(name, peso) '
    'VALUES '
    '(?, ?) '
)
cursor.execute(sql, ['Isabelle', 45])
connection.commit()

cursor.close()
connection.close()