n = int(input("Ingrese el valor deseado: "))
cont = 1
while (cont != n):
    if (n%cont == 0):
        print(f"El numero {n} es divisible por {cont}")
    cont += 1