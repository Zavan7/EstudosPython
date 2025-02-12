from logging import error, warning, critical, debug, info
from logging import basicConfig
from logging import INFO, DEBUG
from pathlib import Path

FILE_LOG = Path(__file__).parent / '.log'

basicConfig(
    level=DEBUG,
    filename=FILE_LOG,
    filemode='a',
    encoding='utf-8',
    format='%(asctime)s %(levelname)s [module:(%(module)s) line:%(lineno)d]: %(message)s',  # noqa E501
    datefmt='%d-%m-%Y %H:%M',
)

error('moio pai')
warning ('agr lascou de vez')
critical ('Volta aqui, a casa caiu')
debug('Fim')
info('testando esse trem')