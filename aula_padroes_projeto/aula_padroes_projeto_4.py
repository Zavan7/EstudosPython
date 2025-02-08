class AppSettings:
    _instance = None

    def __new__ (cls, *arg, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *arg, **kwargs)
        return cls._instance

    def __init__(self):
        self.tema = 'Escuro'
        self.font = '18px'

if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)

