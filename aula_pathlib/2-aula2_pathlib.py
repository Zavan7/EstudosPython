from pathlib import Path

arquivo = Path.home().absolute() / 'OneDrive' / 'Área de Trabalho' / 'texto.txt'

with arquivo.open('a+') as file:
    file.write('vamos testar isso\nparece intereçante\n')
    file.write('vamos testar isso\nparece intereçante\n')

print(arquivo.read_text())