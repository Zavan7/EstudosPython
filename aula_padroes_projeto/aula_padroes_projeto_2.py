from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self)-> None: 
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de LUXO está buscanco nosso cliente VIP.')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de POPULAR está buscanco nosso cliente.')

class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscanco nosso cliente.')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de LUXO está buscanco nosso cliente VIP.')

class VeiculoFactory(ABC):
    def __init__ (self, tipo):
        self.carro = self.get_car(tipo)
    
    @staticmethod 
    @abstractmethod   
    def get_car(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod 
    def get_car(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_pupular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod 
    def get_car(tipo: str) -> Veiculo:
        if tipo == 'carro_pupular':
            return CarroPopular()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    veiculos_zona_norte = [
        'carro_luxo', 
        'carro_pupular', 
        'moto_popular', 
        'moto_luxo'
    ]
    veiculos_sul_norte = [
        'carro_pupular', 
    ]
    print('Zona Norte\n')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_zona_norte))
        carro.buscar_cliente()

    print()
    
    print('Zona Sul\n')
    for i in range(10):
        carro2 = ZonaNorteVeiculoFactory(choice(veiculos_sul_norte))
        carro2.buscar_cliente()