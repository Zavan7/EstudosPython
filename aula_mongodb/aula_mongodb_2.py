from pymongo import MongoClient
import pprint

# Conectar ao MongoDB
cluster = MongoClient("mongodb://localhost:27017/")
db = cluster['Databese']

# Listar todas as coleções no banco de dados 'Database'
colecoes = db.list_collection_names()
print(f"Coleções no banco de dados 'Database': {colecoes}")

# Se 'Collection1' não existir, criar e inserir um documento de teste
if 'Collection1' not in colecoes:
    print("A coleção 'Collection1' não existe. Criando e inserindo um documento de teste.")
    collection = db['Collection1']
    documento_teste = {
        "nome": "Vitor",
        "sobrenome": "Zavan"
    }
    collection.insert_one(documento_teste)
    print(f'Documento inserido: {documento_teste}')

# Consultar a coleção 'Collection1' agora que ela deve existir
collection = db['Collection1']
documentos = collection.find()

# Imprimir os documentos
for doc in documentos:
    pprint.pprint(doc)

