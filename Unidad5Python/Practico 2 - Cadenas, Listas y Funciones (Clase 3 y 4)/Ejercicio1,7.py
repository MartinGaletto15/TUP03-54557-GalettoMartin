lista1 = []
lista2 = []
while True:
    nro = input("Ingrese un numero para la lista 1 (* para salir): ")
    if (nro != '*'):
        nro = int(nro)
        lista1.append(nro)
    else:
        break

while True:
    nro = input("Ingrese un numero para la lista 2 (* para salir): ")
    if (nro != '*'):
        nro = int(nro)
        lista2.append(nro)
    else:
        break

conjunto1 = set(lista1)
conjunto2 = set(lista2)
print(f"interseccion: {conjunto1.intersection(lista2)}")
print(f"difference: {conjunto1.difference(lista2)}")