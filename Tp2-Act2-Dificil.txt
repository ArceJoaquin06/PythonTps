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

print(combinaciones(int(input("Ingrese el número total de personajes: ")), int(input("Ingrese la cantidad de alianzas misticas: "))))