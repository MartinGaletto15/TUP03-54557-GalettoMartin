"""
Crea un programa que pida al usuario su nombre, edad y ciudad, y luego
muestre un mensaje formateado usando f-strings del tipo:
• "Hola, [nombre]. Tienes [edad] años y vives en [ciudad]."
Concepto: Las f-strings (f"...") permiten insertar variables directamente en una
cadena de texto de forma más sencilla y legible
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")
print(f"Hola, {nombre}. Tienes {edad} años y vives en {ciudad}")