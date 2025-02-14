from logging import FileHandler, StreamHandler
from logging import basicConfig
from logging import DEBUG, INFO
from logging import Formatter, Filter, critical, debug
from pathlib import Path

FILE_LOG = Path(__file__).parent / '.log'

class MyFilter(Filter):
    def filter(self, record):
        if record.msg.lower().startswith('senha'):
            return False
        return True

formater_file_hendler = Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s'
)

file_hendler = FileHandler(FILE_LOG, 'w')
file_hendler.setLevel(INFO)
file_hendler.setFormatter(formater_file_hendler)
file_hendler.addFilter(MyFilter())

strem_handler = StreamHandler()
strem_handler.addFilter(MyFilter())

logger = basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(asctime)s %(levelname)s %(message)s',  # noqa E501
    handlers=[file_hendler, strem_handler]
)

debug('olha eu aqui')
critical('senha 1234')
critical('test filtro')
critical('diltro test')