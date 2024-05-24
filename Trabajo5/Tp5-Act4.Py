try:
    num1 = int(input("Ingrese un número entero válido: "))
    num2 = int(input("Ingrese un número entero válido: "))
    sum = num1 + num2
    print(f'La suma de los enteros es {sum}')
except TypeError:
    print("Error: el tipo de dato es inválido")