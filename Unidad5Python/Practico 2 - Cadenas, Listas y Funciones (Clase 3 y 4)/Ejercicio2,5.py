n1 = int(input('Ingrese el numero al que le va a sacar el cuadrado: '))
cuadrado = lambda x: print(x*x)
cuadrado(n1)

lista = [1,2,3,4,5]
lista_cuadrada = list(map(lambda x: x*x, lista))
print(lista_cuadrada)