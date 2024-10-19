def multiplicar(a, b):
    """
    Esta función recibe dos números y retorna su producto.

    Parámetros:
    a (float): El primer número.
    b (float): El segundo número.

    Retorna:
    float: El producto de los dos números.

    Ejemplo:
    >>> multiplicar(2, 3)
    6
    """
    return a * b

# Ejemplo de uso
n1 = int(input("ingres n1: "))
n2 = int(input("ingres n2: "))
resultado = multiplicar(n1, n2)
print(f"El producto de {n1} y {n2} es: {resultado}")