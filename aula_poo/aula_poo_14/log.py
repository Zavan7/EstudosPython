from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'arquivo_log.log'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Succes: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando log', msg_formatada)
        with open(CAMINHO_ARQUIVO, 'a', encoding= 'utf8') as f:
            f.write(msg_formatada)
            f.write('\n')
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
