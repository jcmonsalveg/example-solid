"""
Principio de responsabilidad única

Una clase debe estar como encargada de una única cosa. 

"""

# Creamos la clase estudiantes, cuya única tarea es almacenar los estudiantes en el diccionario
class Estudiantes():
    def __init__(self):
        self.estudiantes = {}
        self.id = 0

    def add_estudiante(self, estudiante):
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


