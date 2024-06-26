import os

def tabla_multi_read():
    while True:
        try:
            n = int(input("Introduce un número entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número ingresado debe ser entre 1 y 10.")
        except ValueError:
            print("Error, introduzca un número entero válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Su tabla de multiplicar de {n} de '{nombre_archivo}' es:")
            print(contenido)
    else:
        print(f"El archivo {nombre_archivo} no existe.")

tabla_multi_read()