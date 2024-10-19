personas = {}

def agregar_persona(nombre, edad):
    personas[nombre] = edad

while True:
    nombre = input("Ingrese el nombre (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input("Ingrese la edad: "))
    agregar_persona(nombre, edad)

print("\nDiccionario de personas:", personas)

nombre_busqueda = input("Ingrese el nombre de la persona cuya edad quiere buscar: ")
edad_busqueda = personas[nombre_busqueda]
print(f"La edad de {nombre_busqueda} es: {edad_busqueda}")
