import math
import os
from itertools import count
def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

caminho = os.path.join('/Users', 'Vtiro Zavan', 'OneDrive', 'Imagens', 'ex')
contador = count()

for root, dirs, files in os.walk(caminho):
    contador_inter = next(contador)
    print (contador_inter, 'Pasta atual', root)

    for dir_ in dirs:
        print ('  ', contador_inter, 'Dir', dir_)

    for file_ in files:
        caminho_comp = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_comp)
        print ('  ', contador_inter, 'Dir', file_, formata_tamanho(tamanho))