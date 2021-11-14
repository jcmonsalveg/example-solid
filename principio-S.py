"""
PRINCIPIO DE RESPONSABILIDAD ÚNICA

Este es el primero de los principios SOLID, y en términos sencillos nos dice que
una clase debe estar encargada de un único proceso dentro de una aplicación, solo
debe hacer una cosa. En mi caso particular podemos ver una aplicación que permite 
tomar los datos de los estudiantes y almacenarlos en un archivo, la primera clase
captura los datos en un diccionario y les asigna un ID,  (una sola cosa) y la segunda 
clase permite guardar los datos en un archivo .txt
"""

# Creamos la clase estudiantes, cuya única tarea es almacenar los estudiantes en el diccionario
class Estudiantes(): #Método constructor
    def __init__(self): 
        self.estudiantes = {}
        self.id = 0

    def add_estudiante(self, estudiante): #Método que agrega el id.
        self.id += 1
        self.estudiantes[self.id] = estudiante

    def __str__(self):
        return str(self.estudiantes)

#Creación de otra clase para el registro de la información en archivo 
class EstudiantesAlmacenados():
    @staticmethod
    def guardar_estudiantes(filename, estudiantes):
        with open(filename, "w") as f:
            f.write(str(estudiantes))

#Implementación de la clase para verificar su funcionamiento
e = Estudiantes()
e.add_estudiante("Diana")  
e.add_estudiante("Simon")
e.add_estudiante("Juan")
e.add_estudiante("Pedro")
print(f"Estudiantes registrados: {e}" ) 

#Implementación de la clase que almacena la info
a = EstudiantesAlmacenados()     
a.guardar_estudiantes("estudiantes.txt", e)
#En la misma carpeta de la aplicación se encuentra el archivo txt


