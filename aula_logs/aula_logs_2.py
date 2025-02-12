from logging import basicConfig
from logging import DEBUG
from logging import debug, info, error
from logging import FileHandler, StreamHandler
from pathlib import Path

FILE_LOG = Path(__file__).parent / '.log'

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(asctime)s %(levelname)s [module:(%(module)s) line:%(lineno)d]: %(message)s',  # noqa E501
    datefmt='%d-%m-%Y %H:%M',
    handlers=[FileHandler(FILE_LOG, 'w'), StreamHandler()]
)

error('ERROR')
debug('DEBUG')
info('INFO')