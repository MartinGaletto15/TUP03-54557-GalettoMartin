#Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.
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


persona1 = Persona('pepito', 25)
persona2 = Persona('jose', 45)
persona1.es_mayor_que(persona2)