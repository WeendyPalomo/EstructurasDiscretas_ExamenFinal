import heapq

def prim_mst(grafo, inicio=0):
    # Formato: {nodo: [(peso, vecino), ...]}
    mst = []
    visitados = set([inicio])
    aristas_candidatas = [(peso, inicio, vecino) for peso, vecino in grafo[inicio]]
    heapq.heapify(aristas_candidatas)

    while aristas_candidatas:
        peso, u, v = heapq.heappop(aristas_candidatas)
        if v not in visitados:
            visitados.add(v)
            mst.append((u, v, peso))
            for proximo_peso, vecino in grafo[v]:
                if vecino not in visitados:
                    heapq.heappush(aristas_candidatas, (proximo_peso, v, vecino))
                    
    return mst
  
grafo_pesos = {
    0: [(4, 1), (8, 2)],
    1: [(4, 0), (3, 2)],
    2: [(8, 0), (3, 1)]
}
print("Prim MST:", prim_mst(grafo_pesos, 0))
