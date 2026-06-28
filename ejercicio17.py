class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, i):
        if self.padre[i] == i:
            return i
        self.padre[i] = self.find(self.padre[i])  # Compresión de caminos
        return self.padre[i]

    def union(self, i, j):
        raiz_i = self.find(i)
        raiz_j = self.find(j)
        if raiz_i != raiz_j:
            if self.rango[raiz_i] < self.rango[raiz_j]:
                self.padre[raiz_i] = raiz_j
            elif self.rango[raiz_i] > self.rango[raiz_j]:
                self.padre[raiz_j] = raiz_i
            else:
                self.padre[raiz_j] = raiz_i
                self.rango[raiz_i] += 1
            return True
        return False

def kruskal_mst(num_vertices, aristas):
    # aristas: lista de tuplas (peso, u, v)
    aristas.sort()
    uf = UnionFind(num_vertices)
    mst = []

    for peso, u, v in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            
    return mst
  
aristas_ejemplo = [(4, 0, 1), (8, 0, 2), (3, 1, 2)]
print("Kruskal MST:", kruskal_mst(3, aristas_ejemplo))
