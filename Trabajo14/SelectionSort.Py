def selectionsort(list, i=0):
    n = len(list)

    if i == n - 1:
        return

    x = find_x(list, i, i + 1, n)

    list[i], list[x] = list[x], list[i]

    selectionsort(list, i + 1)

def find_x(list, j, x, n):
    if j >= n:
        return x
    
    if list[j] < list[x]:
        x = j

    return find_x(list, j + 1, x, n)

list = [4, 2, 3, 1, 7, 5, 6]
selectionsort(list)
print(list)