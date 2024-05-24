try:
    num = int(input("Ingrese un número entero: "))
    print(f'El número ingresado es: {num}')
except ValueError:
    print("Error: el valor es inválido")