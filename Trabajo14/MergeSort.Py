def merge_sort_recursive(list):

    if len(list) <= 1:
        return list
    
    medio = len(list) // 2
    izq = list[:medio]
    der = list[medio:]
    
    izq = merge_sort_recursive(izq)
    der = merge_sort_recursive(der)
    
    return merge(izq, der)

def merge(izq, der):
    result = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            result.append(izq[i])
            i += 1
        else:
            result.append(der[j])
            j += 1
    
    while i < len(izq):
        result.append(izq[i])
        i += 1
    
    while j < len(der):
        result.append(der[j])
        j += 1
    
    return result

list = [2, 7, 4, 5, 1, 3, -4, 9]
list_ord = merge_sort_recursive(list)
print("Lista ya ordenada:", list_ord)

#Para probar: [3.5, 7, 2.7, 4, 6.0, 9.1, 5, 8.1, 0.3, 4.4]