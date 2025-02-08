from pathlib import Path

caaminho = Path()
print(caaminho.absolute())

caaminho_arquivo = Path(__file__)
print(caaminho_arquivo.absolute())
ideias = caaminho_arquivo.parent / 'ideias'

arquivo = Path.home().absolute() / 'OneDrive' / 'Área de Trabalho' / 'texto.txt'
arquivo.touch()
arquivo.write_text('Ola mundo')
print(arquivo.read_text())
arquivo.unlink()

