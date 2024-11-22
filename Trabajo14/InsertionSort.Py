def insertionsort(list, n=None):
    if n is None:
        n = len(list)
    
    if n <= 1:
        return
    
    insertionsort(list, n - 1)
    
    key = list[n - 1]
    j = n - 2
    
    while j >= 0 and list[j] > key:
        list[j + 1] = list[j]
        j -= 1
    
    list[j + 1] = key

list = [6, 1, -1, 5, 3]
insertionsort(list)
print("Lista ya ordenada:", list)

#Para probar: [-3, 2.5, 7, -1.1, 0, 4.7, -8, 6.3, -0.5, 9.8]