try:
    num = int(input("Ingrese un número entero (numerador): "))
    den = int(input("Ingrese un número entero (denominador): "))
    rest = num / den
    print(f'El resultado de la división es: {rest}')
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")