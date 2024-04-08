import math

obj_misterioso = (4, 3)

radio = math.sqrt(obj_misterioso[0]**2 + obj_misterioso[1]**2) 
#el radio es la raiz cuadrada de la suma de las cordenadas al cuadrado

angulo = math.atan2(obj_misterioso[1], obj_misterioso[0])
#el angulo es la tangente de las cordenadas

print("Radio (distancia desde el origen): ", radio)
print("Ángulos (en radianes): ", angulo)

"""
Consigna:
Difícil: Los exploradores necesitan convertir las coordenadas cartesianas de un
objeto misterioso a coordenadas polares para determinar su ubicación exacta en la
isla. Implementa un programa que realice esta conversión utilizando funciones
trigonométricas.
"""