"""
PRINCIPIO DE SEGREGACIÓN DE INTERFAZ

Dice que los usuarios no deben verse obligados a interactuar con interfaces que no utilizan.
Para dar cumplimiento a este principio en Python se utilizan clases y métodos abstractos.
En el código puede verse como ejemplo la creación de subclases que pueden utilizar otros
métodos en la instanciación, por ejemplo el condor no implementa el método nadar.

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
        
class AveNadadora(Ave): #Puede verse que esta clase no implementa el método volar
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

#Instancia de las clases condor y pato con acceso a los métodos volar y nadar
av = condor("ave")
av.volar()

patin = pato("pato")
patin.nadar()

