def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Verificación (fuera de las funciones)
lista = [34, 7, 23, 32, 5, 62]
lista_ordenada = merge_sort(lista)
assert lista_ordenada == sorted(lista), "Error: La lista no está correctamente ordenada."
print("MergeSort exitoso:", lista_ordenada)
