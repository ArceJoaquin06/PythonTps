personas = {'Joaquín': 17, 'Moises': 42, 'Sergio': 56, 'Fede' : 24}

personas['Paris'] = 16 #Agregamos un elemento al diccionario

print("Imprimimos el diccionario con el elemento agregado", personas)

personas.pop('Moises')

print("Imprimimos el diccionario con un elemento eliminado", personas)

print(personas['Joaquín']) #Buscar un value en un elememto

"""
Consigna:
Fácil: Los exploradores llevan un registro de las edades de las personas que
encuentran en la isla. Creen un diccionario con los nombres de las personas y sus
edades, y realizan operaciones como agregar, eliminar y buscar elementos.
"""