nombre_archivo = "tabla_n.txt"
n = int(input("Ingrese un número: "))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    with open(nombre_archivo, 'w') as archivo:
        for i in list:
            if list[0] < n > list[len - 1]:
                archivo.write(str(n))

except IOError:
    print(f"No se pudo abrir el archivo '{nombre_archivo}' en modo escritura.")