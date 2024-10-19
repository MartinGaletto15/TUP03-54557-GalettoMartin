"""
Enunciado: Escribe un programa que pida al usuario una lista de números (separados
por comas) y luego:
1. Muestre la lista original.
2. Ordene la lista de menor a mayor.
3. Elimine el último número de la lista.
4. Añada un nuevo número al inicio de la lista.
"""

numero = input("Ingrese una lista de numeros separados por comas: ")
listaNumeros = list(map(int, numero.split(',')))
print (listaNumeros)
listaNumeros.sort()
print(listaNumeros)
ultimoNro = listaNumeros.pop()
print(listaNumeros)
listaNumeros.insert(0,1)
print(listaNumeros)