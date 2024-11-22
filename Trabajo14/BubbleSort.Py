def bubblesort(list, i=0, j=0):
    n = len(list)

    if i == n-1:
        return
    
    if j == n - i - 1:
        return bubblesort(list, i + 1, 0)
    
    if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
        
    return bubblesort(list, i, j + 1)

list = [4, 2, 3, 1, 6, 5]
bubblesort(list)
print(list)

#Para probar: [5, 3.14, 7, 2.7, 9, 0.9, 4, 1.6, 6, 8.5]