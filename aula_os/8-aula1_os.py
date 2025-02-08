import os
# caminho = r'C:\\Users\\Vtiro Zavan\\OneDrive\\Imagens\\ex'
caminho = os.path.join('/Users', 'Vtiro Zavan', 'OneDrive', 'Imagens', 'ex')

for item in os.listdir(caminho):
    caminho_complite = os.path.join(caminho, item)
    print(item)
    if not os.path.isdir(caminho_complite):
        continue
    for imagem in os.listdir(caminho_complite):
        print ('   ', imagem)