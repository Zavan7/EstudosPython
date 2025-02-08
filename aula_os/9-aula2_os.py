import os
from itertools import count

caminho = os.path.join('/Users', 'Vtiro Zavan', 'OneDrive', 'Imagens', 'ex')
contador = count()

for root, dirs, files in os.walk(caminho):
    contador_inter = next(contador)
    print (contador_inter, 'Pasta atual', root)

    for dir_ in dirs:
        print ('  ', contador_inter, 'Dir', dir_)

    for file_ in files:
        print ('  ', contador_inter, 'Dir', file_)