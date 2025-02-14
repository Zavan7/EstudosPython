from loguru import logger
from pathlib import Path

FILE_LOG = Path(__file__).parent / '.log'

logger.add(FILE_LOG)

logger.debug('DEBUG')
logger.info('INFO')
logger.warning ('WARNING')
logger.error('ERROR')
logger.critical ('CRITICAL')