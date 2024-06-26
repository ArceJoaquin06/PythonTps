def tabla_multi_write():
    try:
        n = int(input("Ingrese un número entero entre 1 y 10: "))
        if n < 1 or n > 10:
            raise ValueError("El número debe estar entre 1 y 10.")
        
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"Su tabla de multiplicar de {n} está guardada en '{nombre_archivo}' exitosamente.")

    except ValueError as ve:
        print(ve)
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}' en modo escritura.")

tabla_multi_write()