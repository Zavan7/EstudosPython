from abc import ABC, abstractmethod
from random import choice


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self)-> None: 
        pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self)-> None: 
        pass

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de LUXO ZN está buscanco nosso cliente VIP.')

class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de LUXO ZN está buscanco nosso cliente VIP.')

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro de POPULAR ZN está buscanco nosso cliente.')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto POPULAR ZN está buscanco nosso cliente.')

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de LUXO ZS está buscanco nosso cliente VIP.')

class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de LUXO ZS está buscanco nosso cliente VIP.')

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro de POPULAR ZS está buscanco nosso cliente.')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto POPULAR ZS está buscanco nosso cliente.')

        
class VeiculoFactory(ABC):    
    @staticmethod 
    @abstractmethod   
    def get_car_luxo() -> VeiculoLuxo:
        pass

    @staticmethod 
    @abstractmethod   
    def get_car_popular() -> VeiculoPopular:
        pass

    @staticmethod 
    @abstractmethod   
    def get_moto_luxo() -> VeiculoLuxo:
        pass

    @staticmethod 
    @abstractmethod   
    def get_moto_popular() -> VeiculoPopular:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod 
    def get_car_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod 
    def get_car_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod    
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod 
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod 
    def get_car_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod 
    def get_car_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod    
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod 
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()

class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_pupular = factory.get_car_popular()
            carro_pupular.buscar_cliente()

            carro_luxo = factory.get_car_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()