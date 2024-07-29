def lineal_search(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

rest = lineal_search([1, 2, 3, 4, 5], int(input("Ingrese un entero: ")))

print(rest)


def binary_search(lista, elemento):
    left = 0
    right = len(lista) - 1
    while left <= right:
        middle = (left + right) // 2
        if lista[middle] == elemento:
            return middle
        elif lista[middle] < elemento:
            left = middle + 1
        else:
            right = middle - 1
    return -1

rest = lineal_search([1, 2, 3, 4, 5], int(input("Ingrese un entero: ")))

print(rest)
