from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class StringMixin:
    def __str__(self):
        parametros = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()\
             if not None and v !=[]]
        )
        return f'{self.__class__.__name__} - ({parametros})'

    def __repr__(self):
        return self.__str__()


class User(StringMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone: List = []
        self.addresses: List = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self) -> User: pass

    @abstractmethod
    def add_firstname(self, firstname)-> UserBuilder: pass
    
    @abstractmethod
    def add_lastname(self, lastname)-> UserBuilder: pass
    
    @abstractmethod
    def add_age(self, age)-> UserBuilder: pass
    
    @abstractmethod
    def add_phone(self, phone)-> UserBuilder: pass
        
    @abstractmethod
    def add_addresses(self, addresses)-> UserBuilder: pass
    
class UserBuilder(IUserBuilder):
    def __init__(self)-> None:
        self.reset()

    def reset(self)-> None:
        self._result = User()

    @property
    def result(self): 
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname)-> UserBuilder:
        self._result.firstname = firstname
    
    def add_lastname(self, lastname)-> UserBuilder:
        self._result.lastname = lastname

    def add_age(self, age)-> UserBuilder:
        self._result.age = age
   
    def add_phone(self, phone)-> UserBuilder:
        self._result.phone.append(phone)
       
    def add_addresses(self, addresses)-> UserBuilder:
        self._result.addresses.append(addresses)


class UserDirector:
    def __init__(self, builder)-> None:
        self._builder = builder

    def with_age(self, firstname, lastname, agr) -> User:
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(agr)
        return self._builder.result

    def with_adresses(self, firstname, lastname, addresses) -> User:
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_addresses(addresses)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Vitor', 'Zavan', 28)
    user2 = user_director.with_adresses('Isabelle', 'Zavan', ('Av Brasil', 'Av SP'))

    print(user1)
    print(user2)