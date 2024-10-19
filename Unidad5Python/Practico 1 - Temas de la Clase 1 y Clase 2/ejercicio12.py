nota = float(input("Introduce la nota (0-10): "))
while (nota < 0 or nota > 10):
    print("Numero no valido ingrese otro")
    nota = float(input("Introduce la nota (0-10): "))

if 0 <= nota < 3:
    calificacion = "Muy deficiente"
elif 3 <= nota < 5:
    calificacion = "Insuficiente"
elif 5 <= nota < 6:
    calificacion = "Suficiente"
elif 6 <= nota < 7:
    calificacion = "Bien"
elif 7 <= nota < 9:
    calificacion = "Notable"
elif 9 <= nota <= 10:
    calificacion = "Sobresaliente"
else:
    calificacion = "Nota no valida"

print(f"La calificación es: {calificacion}")