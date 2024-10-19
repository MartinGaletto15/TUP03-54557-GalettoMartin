n = int(input("Ingrese el valor deseado: "))
cont = 0
for i in range(1,n+1):
    if (n%i == 0):
        print(f"El numero {n} es divisible por {i}")
        cont += 1
if(cont == 2):
    print("El numero es primo :D")