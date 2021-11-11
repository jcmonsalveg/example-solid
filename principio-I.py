"""
Principio de Segregación de Interfaz. 

Dice que los usuarios no deben verse obligados a interactuar con interfaces que no utilizan.

Elaborado a partir del ejemplo de: 
https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/ Modificado
"""

from abc import ABC, abstractmethod

class Ave(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sonido(self) -> str:
        pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        print(f"{self.name} Me gusta volar por el cielo")
        
class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        print(f"{self.name} Estoy nadando")

class condor(AveVoladora):
    def volar(self):
        print(f"{self.name} Vuelo mucho")

    def sonido(self) -> str:
        return "Sonido condor"

class pato(AveNadadora, AveVoladora): 
    def volar(self):
        print(f"{self.name} Vuela")

    def nadar(self):
        print(f"{self.name} nada en la piscina")

    def sonido(self) -> str:
        return "sonido pato"


av = condor("ave")
av.volar()