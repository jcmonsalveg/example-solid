"""
El principio de Substitución de LISKOV. 

Los objetos deben poder ser reemplazados por instancias de sus subclases sin que
afecte el correcto funcionamiento del sistema.
"""

class Car:
    @staticmethod
    def asientos()->int:
        pass

class Renault(Car):
    @staticmethod
    def asientos() -> int:
        return 2

class Audi(Car):
    @staticmethod
    def asientos() -> int:
        return 4

if __name__ =="__main__":
    print(Renault.asientos())
    print(Audi.asientos())