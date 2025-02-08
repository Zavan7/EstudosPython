# diretórios = pasta do PC
# root = diretório atual
# dirs = lista de subdiretorios
# files = arquivos de diretorios atuais

import os
import shutil

HOME = os.path.expanduser('~')
AREADETRABALHO = os.path.join (HOME, 'OneDrive', 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join (AREADETRABALHO, 'EXEMPLO')
NOVA_PASTA = os.path.join (AREADETRABALHO, 'NOVA PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)

        os.makedirs(caminho_novo_diretorio, exist_ok=True)


    for file in files:
        caminho_original = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        print(caminho_novo_arquivo)
        shutil.copy(caminho_original, caminho_novo_arquivo)
