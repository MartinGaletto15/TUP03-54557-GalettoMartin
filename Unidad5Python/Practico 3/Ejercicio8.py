'''
Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicación y
división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
'''

class Calculadora():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def calculos(self):
        self.suma = self.n1 + self.n2
        self.diferencia = self.n1 - self.n2
        self.producto = self.n1 * self.n2
        self.division = self.n1 / self.n2
    def mostrarCalculos(self):
        self.calculos()
        print(f'Suma = {self.suma}')
        print(f'Diferencia = {self.diferencia}')
        print(f'Producto = {self.producto}')
        print(f'Division = {self.division}')

calculadora = Calculadora(5, 7)
calculadora.mostrarCalculos()