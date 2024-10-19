n1 = int(input("Ingrese el primer nro: "))
n2 = int(input("Ingrese el segundo nro: "))

if(n1 == n2):
    print("Son iguales")
elif(n1 < n2):
    print(f"{n1} < {n2}")
else:
    print(f"{n2} < {n1}")