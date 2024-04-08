power = int(input("Ingresa la cantidad de tu poder: "))
life = int(input("Ingresa la cantidad de vida de tu adversario: "))

if power > life:
  print("Derrotaste a tu enemigo!")
elif power == life: 
  print("Empate! tu y tu adversario empataron y se dieron cuenta la cantidad de cosas en común que tienen los dos y deciden formar una familia")
elif power < life: 
  print("Tu enemigo te derrotó!")

"""
Consigna:
Intermedio: Los magos necesitan calcular la potencia de sus hechizos para derrotar
a los enemigos. Pide al usuario que ingrese la potencia de un hechizo y el nivel de
resistencia del enemigo. Calcula y muestra si el hechizo es lo suficientemente fuerte
para derrotar al enemigo.
"""