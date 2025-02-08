from contextlib import contextmanager
from wasabi import msg
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula_poo_23.txt'


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        msg.info('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo

    except Exception as e:
        msg.fail('Ocorreu erro', e)

    finally:
        msg.info('Fechando arquivo')
        arquivo.close()


with my_open(CAMINHO_ARQUIVO, 'w') as arquivo:
    arquivo.write('Tentando \n')
    arquivo.write('Tentando \n')
    arquivo.write('Tentando \n', 123)
    arquivo.write('Tentando \n')
    print('WITH', arquivo)