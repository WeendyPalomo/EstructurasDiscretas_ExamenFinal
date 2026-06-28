def dfs_iterativo(grafo, inicio):
    visitados = set()
    pila = [inicio]
    recorrido = []

    while pila:
        vertice = pila.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            recorrido.append(vertice)
            pila.extend(reversed([v for v in grafo[vertice] if v not in visitados]))
            
    return recorrido

# Ejemplo de Búsqueda (fuera de la función, pegado a la izquierda)
grafo_busqueda = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2]}
print("DFS:", dfs_iterativo(grafo_busqueda, 0))
