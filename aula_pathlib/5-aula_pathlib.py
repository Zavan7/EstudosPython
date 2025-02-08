'''Continuação da aula 4, agora removendo a pasta criada na aula anterior'''
from pathlib import Path
from shutil import rmtree

caminho_pasta = Path.home() / 'OneDrive' / 'Área de Trabalho' / 'Pasta Exemplo'
caminho_pasta.mkdir(exist_ok= True)

files = caminho_pasta / 'files'
files.mkdir(exist_ok= True)

for i in range (10):
    file = files /f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Óla mundo!\n')
        text_file.write(f'file_{i}.txt')

def rmtree(root: Path, remove_root = True):
    for file in root.glob('*'):
        if file.is_dir():
            print('Dir:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('File:', file)
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)