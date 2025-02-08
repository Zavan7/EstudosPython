from pathlib import Path

caminho_pasta = Path.home() / 'OneDrive' / 'Área de Trabalho' / 'Pasta Exemplo'
caminho_pasta.mkdir(exist_ok= True)

sub_pasta = caminho_pasta / 'subpasta'
sub_pasta.mkdir(exist_ok= True)

arquivo = sub_pasta / 'arquivo.txt'
arquivo.touch()
arquivo.write_text('ola')

arquivo1 = caminho_pasta / 'arquivo1.txt'
arquivo1.touch()
arquivo.write_text('ola')

caminho_pasta.rmdir()