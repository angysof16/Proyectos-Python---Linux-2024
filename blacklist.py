def print_menu():
    print("\nMenú:")
    print("1. Ver contactos que me caen bien")
    print("2. Ver contactos que me caen mal")
    print("3. Agregar un contacto")
    print("4. Eliminar un contacto")
    print("5. Buscar un contacto por nombre")
    print("6. Salir")

def ver_contactos(filtro):
    for contacto in agenda:
        if agenda[contacto]['estado'] == filtro:
            print(f"\nNombre: {contacto}, Teléfono: {agenda[contacto]['telefono']}, Dirección: {agenda[contacto]['direccion']}, Estado: {agenda[contacto]['estado']}")

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    while True:
        print("Estado del contacto:")
        print("1. Me cae bien")
        print("2. Me cae mal")
        estado_opcion = int(input("Elige una opción (1-2): "))
        if estado_opcion == 1:
            estado = 'me cae bien'
            break
        elif estado_opcion == 2:
            estado = 'me cae mal'
            break
        else:
            print("Opción inválida. Por favor ingrese 1 o 2.")
    agenda[nombre] = {'telefono': telefono, 'direccion': direccion, 'estado': estado}
    print(f"Contacto {nombre} agregado exitosamente.")

def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"\nContacto {nombre} eliminado exitosamente.")
    else:
        print(f"\nEl contacto {nombre} no fue encontrado.")

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"\nNombre: {nombre}, Teléfono: {contacto['telefono']}, Dirección: {contacto['direccion']}, Estado: {contacto['estado']}")
    else:
        print(f"\nEl contacto {nombre} no fue encontrado.")

agenda = {}
menu_choice = 0

while menu_choice != 6:
    print_menu()
    menu_choice = int(input("Elige una opción (1-6): "))
    
    if menu_choice == 1:
        print("Contactos que me caen bien:")
        ver_contactos('me cae bien')
    elif menu_choice == 2:
        print("Contactos que me caen mal:")
        ver_contactos('me cae mal')
    elif menu_choice == 3:
        agregar_contacto()
    elif menu_choice == 4:
        eliminar_contacto()
    elif menu_choice == 5:
        buscar_contacto()
    elif menu_choice == 6:
        print("Saliendo de la agenda...")
    else:
        print("Opción inválida. Por favor ingrese un número del 1 al 6.")
