'''
Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.
'''
#https://docs.python.org/es/3/tutorial/classes.html

class persona():
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_edad(self, edad):
        self.edad = edad
    def get_nombre(self):
        print(self.nombre)
    def get_edad(self):
        print(self.edad)
    def print_persona(self):
        print(f'Nombre: {self.nombre}. Edad: {self.edad}')

persona1 = persona()
persona1.set_nombre('Pepito')
persona1.set_edad(21)
persona2 = persona()
persona2.set_nombre('Gustavo')
persona2.set_edad(75)

persona1.print_persona()
persona2.print_persona()