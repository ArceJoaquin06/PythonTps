import os

def listin_create():
    if not os.path.exists("listin.txt"):
        with open("listin.txt", 'w') as archivo:
            pass 
        print("Archivo listin.txt creado.")
    else:
        print("El archivo listin.txt ya existe.")

def phone_consultate(nombre_cliente):
    if os.path.exists("listin.txt"):
        with open("listin.txt", 'r') as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(',')
                if nombre.lower() == nombre_cliente.lower():
                    print(f"El teléfono de {nombre_cliente} es {telefono}.")
                    return
            print(f"El cliente {nombre_cliente} no está en el listín.")
    else:
        print("El archivo listin.txt no existe.")

def user_toAdd(nombre_cliente, telefono):
    with open("listin.txt", 'a') as archivo:
        archivo.write(f"{nombre_cliente},{telefono}\n")
    print(f"Cliente {nombre_cliente} añadido con el teléfono {telefono}.")

def user_eliminate(nombre_cliente):
    if os.path.exists("listin.txt"):
        lineas = []
        encontrado = False
        with open("listin.txt", 'r') as archivo:
            lineas = archivo.readlines()
        
        with open("listin.txt", 'w') as archivo:
            for linea in lineas:
                nombre, telefono = linea.strip().split(',')
                if nombre.lower() != nombre_cliente.lower():
                    archivo.write(f"{nombre},{telefono}\n")
                else:
                    encontrado = True
        
        if encontrado:
            print(f"Cliente {nombre_cliente} ha sido eliminado del listín.")
        else:
            print(f"El cliente {nombre_cliente} no se encuentra en el listín.")
    else:
        print("El archivo listin.txt no existe.")

def menu():
    listin_create()
    while True:
        print("\nGestión de Listín Telefónico")
        print("1. Consultar al teléfono")
        print("2. Añadir un cliente")
        print("3. Eliminar un cliente")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre_cliente = input("Introduce el nombre del cliente: ")
            phone_consultate(nombre_cliente)
        elif opcion == '2':
            nombre_cliente = input("Introduzca el nombre del cliente por añadir: ")
            telefono = input("Introduzca el teléfono del cliente por añadir: ")
            user_toAdd(nombre_cliente, telefono)
        elif opcion == '3':
            nombre_cliente = input("Introduzca el nombre del cliente a eliminar: ")
            user_eliminate(nombre_cliente)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Error. Por favor, selecciona una opción del 1 al 4.")

menu()