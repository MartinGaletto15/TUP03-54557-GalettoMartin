# Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.

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
    
    def es_mayor_que(self, objeto):
        if(self.edad > objeto.edad):
            print(f'{self.nombre} > {objeto.nombre}')
        else:
            print(f'{self.nombre} < {objeto.nombre}')

    @staticmethod
    def get_mayor(x, y):
        if(x.edad > y.edad):
            print(f'{x.nombre} > {y.nombre}')
        else:
            print(f'{x.nombre} < {y.nombre}')



persona1 = Persona('pepito', 25)
persona2 = Persona('jose', 45)
Persona.get_mayor(persona1, persona2)