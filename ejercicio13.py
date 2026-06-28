def dfs_conectividad(nodo, grafo, visitados):
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_conectividad(vecino, grafo, visitados)

def tiene_circuito_euleriano(grafo):
    # 1. Verificar que todos los grados sean pares
    for nodo, vecinos in grafo.items():
        if len(vecinos) % 2 != 0:
            return False

    # 2. Verificar conectividad de los nodos con aristas
    nodos_con_aristas = [n for n, v in grafo.items() if len(v) > 0]
    if not nodos_con_aristas: 
        return True

    visitados = set()
    dfs_conectividad(nodos_con_aristas[0], grafo, visitados)

    return all(n in visitados for n in nodos_con_aristas)

grafo_euleriano = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [2, 3]}
print("¿Tiene circuito de Euler?:", tiene_circuito_euleriano(grafo_euleriano))
