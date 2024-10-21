class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def anadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} añadido.")

    def listar_contactos(self):
        if self.contactos:
            for idx, contacto in enumerate(self.contactos, 1):
                print(f"{idx}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
        else:
            print("No hay contactos en la agenda.")

    def buscar_contacto(self, email):
        for contacto in self.contactos:
            if contacto.email == email:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return contacto
        print("Contacto no encontrado.")
        return None

    def editar_contacto(self, email):
        contacto = self.buscar_contacto(email)
        if contacto:
            print("1. Editar nombre")
            print("2. Editar teléfono")
            print("3. Editar email")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ")
                contacto.nombre = nuevo_nombre
            elif opcion == "2":
                nuevo_telefono = input("Nuevo teléfono: ")
                contacto.telefono = nuevo_telefono
            elif opcion == "3":
                nuevo_email = input("Nuevo email: ")
                contacto.email = nuevo_email
            else:
                print("Opción no válida.")
            print(f"Contacto {contacto.nombre} actualizado.")
    
    def mostrar_menu(self):
        while True:
            print("\n1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.anadir_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                nombre = input("Email del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Email del contacto a editar: ")
                self.editar_contacto(nombre)
            elif opcion == "5":
                print("Gracias por usar nuestra agenda")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


agenda = Agenda()
agenda.mostrar_menu()
