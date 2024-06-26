from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = None
    try:
        archivo = open(ruta_archivo, modo)
        yield archivo
    finally:
        if archivo:
            archivo.close()

def leer_archivo(ruta_archivo):
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def escribir_archivo(ruta_archivo, lineas):
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            archivo.write(linea + '\n')


if __name__ == "__main__":
    ruta = 'MiArchivoInsano.txt'
    saludo = ["En la radio, hay un pollito En la radio, hay un pollito El pollito pío, el pollito pío El pollito pío, el pollito pío El pollito pío, el pollito pío En la radio, hay una gallina En la radio, hay una gallina Y la gallina coo, y el pollito pío Y el pollito pío, y el pollito pío Y el pollito pío, y el pollito pío En la radio, hay también un gallo En la radio, hay también un gallo Y el gallo corococo, y la gallina coo Y el pollito pío, el pollito pío El pollito pío, el pollito pío"]
    
    escribir_archivo(ruta, saludo)
    
    leer_archivo(ruta)