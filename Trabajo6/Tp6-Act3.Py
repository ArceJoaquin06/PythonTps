import os

def tabla_multi_readline():
    while True:
        try:
            n = int(input("Escriba un número 'n' entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe ser entre 1 y 10.")
        except ValueError:
            print("Error, introduzca un número entero válido.")
    
    while True:
        try:
            m = int(input("Escriba otro número 'm' entero entre 1 y 10: "))
            if 1 <= m <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Error, introduzca un número entero válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print("Su linea solicitada es:", lineas[m-1].strip())
                else:
                    print(f"El archivo {nombre_archivo} no tiene {m} líneas.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

tabla_multi_readline()