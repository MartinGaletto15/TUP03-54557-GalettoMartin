frase = input("Ingrese la frase: ")
frase = frase.upper()
print(frase)
print(frase.count('A'))
vocales = "AEIOU"
for vocal in vocales:
    frase = frase.replace(vocal, "*")
print(frase.lower())