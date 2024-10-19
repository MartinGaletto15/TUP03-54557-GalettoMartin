def saludo(nombre, saludar = "Hola"):
    print(f'{saludar}, {nombre}')

nombre = input("Ingrese su nonmbre: ")
saludar = input("Ingrese el saludo opcional (* para omitir): ")
if(saludar == "*"):
    saludo(nombre)
else:
    saludo(nombre, saludar)