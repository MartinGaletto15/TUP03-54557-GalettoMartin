for i in range(1, 501):
    # Verificar si el número es múltiplo de 4 o de 9
    if i % 4 == 0 and i % 9 == 0:
        print(f"{i} (Múltiplo de 4 y de 9)")
    elif i % 4 == 0:
        print(f"{i} (Múltiplo de 4)")
    elif i % 9 == 0:
        print(f"{i} (Múltiplo de 9)")
    else:
        print(i)
    
    # Cada 5 líneas, imprimir una línea horizontal
    if i % 5 == 0:
        print("-" * 60)
