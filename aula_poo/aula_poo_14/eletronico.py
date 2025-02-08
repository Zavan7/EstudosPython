from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False


    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

    def mudar_canal(self):
        print ('Mudou de canal')


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)

class Televisao(Eletronico, LogFileMixin):
    def mudar_canal(self):
        super().mudar_canal()
        msg = 'Mudou de canal'
        self.log_success(msg)
         