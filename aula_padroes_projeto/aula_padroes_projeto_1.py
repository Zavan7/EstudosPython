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

class VeiculoFactory:
    def __init__ (self, tipo):
        self.carro = self.get_car(tipo)
    
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

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    carros_livres = ['carro_luxo', 'carro_pupular', 'moto_popular', 'moto_luxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_livres))
        carro.buscar_cliente()


