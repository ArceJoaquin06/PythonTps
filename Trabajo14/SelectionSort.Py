def selectionsort(list, i=0, j=0, x=0):
    n = len(list)

    if i == n-1:
        return

    if j == n - i - 1:
        list[i] = x
        return selectionsort(list, i + 1, 0, 0)
    
    if list[j] > list[j + 1] and x <= list[j + 1]:
        x = list[j+1]
    
    if list[j] > list[j + 1] and x >= list[j + 1]:
        x = list[j+1]

    return selectionsort(list, i, j + 1, x)

list = [4, 2, 3, 1, 7, 5, 6]
selectionsort(list)
print(list)