"""
Principio de abierto / cerrado

Los componentes del software deben estar abiertos para su extensión, pero cerrados para su modificación. 

"""

from abc import ABC, abstractmethod
from typing import Sequence, List

class Car(ABC):
    @abstractmethod
    def car_price(self)->int:
        pass

class Renault(Car):
    def car_price(self) -> int:
        return 18000

class Audi(Car):
    def car_price(self) -> int:
        return 25000

class Mercedes(Car):
    def car_price(self) -> int:
        return 27000

def main() -> None:
    car_list: List[Car] = [Renault(), Audi(), Mercedes()]

    print_car_price(car_list)

def print_car_price(car_list: Sequence[Car]) -> None:
    for coche in car_list:
        print(coche.car_price())

if __name__ =="__main__":
    main()





