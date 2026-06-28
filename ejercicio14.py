from collections import deque

def bfs(grafo, inicio):
    visitados = set([inicio])
    cola = deque([inicio])
    recorrido = []

    while cola:
        vertice = cola.popleft()
        recorrido.append(vertice)

        for vecino in grafo[vertice]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                
    return recorrido

# Ejemplo de Búsqueda (fuera de la función, pegado a la izquierda)
grafo_busqueda = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2]}
print("BFS:", bfs(grafo_busqueda, 0))
