#Agregarle a la clase anterior un constructor que reciba nombre y edad.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


persona1 = Persona('pepito', 25)
persona1.print_persona()