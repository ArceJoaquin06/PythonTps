list = [1, 2, 3, 4, 5]

try:
    print("El numero de la lista corresponde a: ", list[int(input("Ingrese un número entero: "))])
except IndexError:
    print("Error: El índice introducido está fuera de rango")