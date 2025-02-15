from loguru import logger
from pathlib import Path
import sys

FILE_LOG = Path(__file__).parent / '.log'

logger.remove()

def filtro_senha(record):
    if 'senha' in record['message']:
        return False
    return True

logger.add(
    sys.stderr,
    format='{time} - <r>{level}</r> - <g>{message}</g> - {file} - {line}', 
    filter= filtro_senha
)

logger.debug('DEBUG')
logger.info('INFO')
logger.warning ('WARNING')
logger.error('ERROR')
logger.critical('senha')