def catalogar():
    for pepe in vehiculos:
        print(vars(pepe))

def catalogar2(nro):
    cont = 0
    for pepe in vehiculos:
        print(vars(pepe))
        if(pepe.ruedas == nro):
            cont += 1
    print(f'Se han encontrado {cont} vehiculos con {nro} ruedas')

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

autito = Coche("rojo", 4, 200, 200)
bicicletita = Bicicleta("rojo", 2, "urbana")
vehiculos = [
    autito,
    bicicletita,
    Motocicleta("rojo", 2, "urbana", 200, 4000),
    Camioneta("rojo", 4, 200, 4000, 5000)
]

# Ejercicio 2: Mostrar los atributos de cada objeto en la lista vehiculos
catalogar()
# Ejercicio 3
nroRuedas = int(input("Ingrese la cantidad de ruedas: "))
catalogar2(nroRuedas)