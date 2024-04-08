lista = [10,2,3,7,5,6,5,8,3,10]
list_rest = []

def listas(lista):
  for i in lista:
    if i not in list_rest:
      list_rest.append(i)
  return list_rest

print(listas(lista))

"""
Consigna:
Intermedio: Durante su expedición, los aventureros recolectan una variedad de
cristales preciosos. Sin embargo, descubren que algunos cristales están duplicados
en su inventario. Deben eliminar los cristales duplicados para tener una lista única.
"""