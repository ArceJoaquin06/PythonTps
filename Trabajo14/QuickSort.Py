def quicksort(list):

    if len(list) <= 1:
        return list
    
    pivote = list[-1]
    
    izq = [x for x in list[:-1] if x <= pivote]
    der = [x for x in list[:-1] if x > pivote]
    
    return quicksort(izq) + [pivote] + quicksort(der)

list = [-4, 3, 1, 5, 2, 7, 0]
list_ord = quicksort(list)
print("Lista ya ordenada:", list_ord)

#Para probar: [-1, 0.03, 4, -2.5, 9, 0.6, -6, 1.9, 3, 5.5]