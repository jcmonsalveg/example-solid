"""
PRINCIPIO DE SUSTITUCIÓN DE LISKOV

Los objetos deben poder ser reemplazados por instancias de sus subclases sin que
afecte el correcto funcionamiento del sistema. Es decir, pasar objetos de las 
clases hijas o subclases, en lugar de objetos directos de la clase padre.


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