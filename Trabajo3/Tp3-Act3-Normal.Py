inscrips = ['M','F','J','P','S','M','J','M','P']

frequency = {}

for inscrip in inscrips:
    if inscrip in frequency:
        frequency[inscrip] += 1
    else:
        frequency[inscrip] = 1

print("Frecuencia  de letras: ", frequency)

"""
Consigna:
Intermedio: Durante su expedición, los exploradores encuentran una inscripción
antigua en un templo. Deben contar la frecuencia de cada letra en la inscripción
utilizando un diccionario.
"""