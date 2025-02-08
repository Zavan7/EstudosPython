from __future__ import annotations
from copy import deepcopy
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

class Address(StringMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number

class Person(StringMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List [Address] = []
    
    def add_addresses(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)

if __name__ == '__main__':
    vitor = Person('Vitor', 'Zavan')
    end_vitor = Address('Av Brasil', '123')
    vitor.add_addresses(end_vitor)

    esposa_vitor = vitor.clone()
    esposa_vitor.firstname = 'Isabelle'

    print(vitor)
    print(esposa_vitor)