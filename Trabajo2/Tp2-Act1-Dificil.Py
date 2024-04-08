def factorial(n):
  if n == 0 or n == 1:
    return 1
  else: 
    return n * factorial(n-1)

def combinaciones(n, k):
  if k > n:
    return 0
  else:
    return factorial(n) // (factorial(k) * factorial(n-k))

print(combinaciones(int(input("Ingrese el número total de personas: ")), int(input("Ingrese el tamaño del equipo: "))))

"""
Consigna:
Difícil: Los astronautas necesitan determinar cuántas combinaciones diferentes de
equipos pueden formar con un grupo de personas para las misiones en la Luna.
Opcional: Implementa una función llamada calcular_combinaciones() que
reciba el número total de personas y el tamaño del equipo, y devuelva el número
total de combinaciones posibles.
"""