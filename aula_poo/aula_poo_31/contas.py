import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R$ {valor})')
        return self.saldo
    
    def detalhes(self, msg: str = '')-> None:
        print(f'Seu saldo é: R$ {self.saldo:.2f}')
        print('_' * 50)

    def __repr__ (self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}, {attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE: R$ {valor}')
            return self.saldo
        
        print('Saldo insuficiente')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int,
              saldo: float = 0, limite: float = 0
    ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'SAQUE: R$ {valor}')
            return self.saldo
        
        print('Saldo insuficiente')
        print(f'Seu limite é de R$ {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

    def __repr__ (self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r}'
        return f'{class_name}, {attrs}'
        
            
if __name__ == '__main__':
    # cp = ContaPoupanca(1111, 25458)
    # cp.depositar(1000)
    # cp.sacar(500)
    # cp.sacar(500)
    # cp.sacar(500)
    # print('#' * 50)
    cc1 = ContaCorrente(1111, 25458, 0, 500)
    cc1.depositar(1000)
    cc1.sacar(500)
    cc1.sacar(500)
    cc1.sacar(500)
    cc1.sacar(500)
    print('#' * 50)