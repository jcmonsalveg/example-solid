"""
El principio de inversión de dependencias. 

Es el último de los principios SOLID. Parte de dos reglas: las clases de alto nivel no deben depender de las
clases de bajo nivel, ambas deben depender de las abstracciones. Las abstracciones no deben depender de los detalles,
son los detalles los cuales dependen de las abstracciones.

Con el objetivo de facilitar la comprensión del concepto, trabajé con el código del video: 
https://www.youtube.com/watch?v=Kv5jhbSkqLE

La definición de clases abstractas y de métodos abstractos es el mecanismo que se puede emplear en Python para
dar cumplimiento a este principio. 

"""

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):    
        pass

class Bombillo(Switchable): #Aquí vemos como depende de la abstracción
    def encender(self):
        print("Bombillo encendido...")

    def apagar(self):
        print("Bombillo apagado...")

class Encendedor:

    def __init__(self, c: Switchable): #Depende de la abstracción
        self.client = c
        self.on = False

    def presionar(self):
        if self.on:
            self.client.apagar()
            self.on = False
        else:
            self.client.encender()
            self.on = True


b = Bombillo()
switch = Encendedor(b)
switch.press()
switch.press()


        